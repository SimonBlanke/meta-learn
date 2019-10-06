# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import inspect
import os
import pandas as pd
import hashlib

from ...data_wrangler import merge_meta_data

from ._dataset_features import DatasetFeatures
from ._model_features import ModelFeatures


class Collector:
    def __init__(self, search_config, n_jobs=1, meta_data_path=None):
        self.search_config = search_config
        self.n_jobs = n_jobs
        self.meta_data_path = meta_data_path

        self.collector_model = ModelFeatures(self.search_config)

    def extract(self, X, y, _cand_list):
        self.collector_dataset = DatasetFeatures()

        for model_func in self.search_config.keys():

            func_str = self._get_func_str(model_func)

            meta_data = self._get_meta_data(model_func, [X, y], _cand_list)
            self._save_toCSV(meta_data, func_str, self._get_hash(X))

    def _get_hash(self, object):
        return hashlib.sha1(object).hexdigest()

    def _get_func_str(self, func):
        return inspect.getsource(func)

    def _get_meta_data(self, model_name, data_train, _cand_list):
        X = data_train[0]
        y = data_train[1]

        md_model = self.collector_model.collect(model_name, X, y, _cand_list)
        md_dataset = self.collector_dataset.collect(model_name, data_train)

        meta_data = merge_meta_data(md_dataset, md_model)

        return meta_data

    def _save_toCSV(self, meta_data_new, func_str, data_hash):
        if not os.path.exists(self.meta_data_path):
            os.makedirs(self.meta_data_path)

        print(func_str.encode("utf-8"))

        file_name = (
            "metadata_func_hash="
            + self._get_hash(func_str.encode("utf-8"))
            + "_data_hash="
            + data_hash
            + "_.csv"
        )
        path = self.meta_data_path + file_name

        print("meta_data_new", meta_data_new)

        if os.path.exists(path):
            meta_data_old = pd.read_csv(path)
            meta_data = meta_data_old.append(meta_data_new)

            columns = list(meta_data.columns)
            noScore = ["mean_test_score", "cv_default_score"]
            columns_noScore = [c for c in columns if c not in noScore]

            meta_data = meta_data.drop_duplicates(subset=columns_noScore)
        else:
            meta_data = meta_data_new

        meta_data.to_csv(path, index=False)
