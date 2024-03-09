# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import os
import shutil
import itertools
from typing import Tuple

import pandas as pd


from .paths import Paths
from .search_data import SearchData
from .dataset_features import DatasetFeatures


class BaseMetaData:
    def __init__(self, path):
        self.path = Paths(path)

        self.dataset_feature_generator = None

    def remove(self, model_id=None, dataset_id=None):
        if model_id and dataset_id:
            shutil.rmtree(self.path.get_dataset_dir(model_id, dataset_id))
        elif model_id:
            shutil.rmtree(self.path.get_model_dir(model_id))
        elif not model_id and not dataset_id:
            shutil.rmtree(self.path.base_path_name)
        else:
            raise ValueError

    def collect(self, X, y, model_id, dataset_id):
        self.search_data = SearchData(model_id, dataset_id)
        self.dataset_features = DatasetFeatures(model_id, dataset_id)

        ref_scores = self.dataset_feature_generator.create(X, y)
        self.dataset_features.dump(ref_scores)

        def decorator(model):
            def wrapper(access):
                parameter = access.para_dict

                result = model(access)

                if isinstance(result, tuple):
                    parameter["score"] = result[0]
                    parameter.update(result[1])
                else:
                    parameter["score"] = result

                self.search_data.append(parameter)

                return result

            return wrapper

        return decorator

    def get_meta_data_X(self, search_space, X, y):
        print("\n approx_best_para")

        keys, values = zip(*search_space.items())
        permutations_dicts = [dict(zip(keys, v)) for v in itertools.product(*values)]

        all_parameters = pd.DataFrame(permutations_dicts)

        ref_scores = self.dataset_feature_generator.create(X, y)
        meta_data_test = all_parameters.assign(**ref_scores)

        print("create", len(all_parameters), "samples")
        return meta_data_test

    def get_meta_data(self, model_id: str) -> Tuple[pd.core.frame.DataFrame]:
        model_dir = self.path.get_model_dir(model_id)
        dataset_id_l = [name for name in os.listdir(model_dir)]

        meta_data_train_l = []
        for dataset_id in dataset_id_l:
            dataset_path = os.path.join(model_dir, dataset_id)

            dataset_features_path = os.path.join(dataset_path, "dataset_features.json")
            search_data_path = os.path.join(dataset_path, "search_data.csv")

            with open(dataset_features_path, "r") as f:
                ref_scores = json.load(f)

            search_data = pd.read_csv(search_data_path)

            meta_data_train = search_data.assign(**ref_scores)
            meta_data_train_l.append(meta_data_train)

        meta_data_train = pd.concat(meta_data_train_l, axis=0, ignore_index=True)
        print("Found", len(meta_data_train), "samples")

        meta_data_X = meta_data_train.drop("score", axis=1)
        meta_data_y = meta_data_train["score"]

        return meta_data_X, meta_data_y
