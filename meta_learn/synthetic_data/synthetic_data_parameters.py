# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

"""
dataset_dict = {
    "test_dataset_0": {
        "n_samples": 300,
        "n_features": 10,
        "n_informative": 4,
        "class_sep": 0.9,
        "n_classes": 3,
        "flip_y": 0.3,
    },
    "test_dataset_1": {
        "n_samples": 500,
        "n_features": 12,
        "n_informative": 8,
        "n_redundant": 3,
        "class_sep": 1.0,
        "n_clusters_per_class": 3,
        "flip_y": 0.1,
    },
    "test_dataset_2": {
        "n_samples": 1000,
        "n_features": 14,
        "n_informative": 5,
        "n_redundant": 4,
        "n_repeated": 2,
        "class_sep": 0.5,
        "n_classes": 4,
        "flip_y": 0.1,
    },
    "test_dataset_3": {
        "n_samples": 2000,
        "n_features": 15,
        "n_informative": 3,
        "n_redundant": 3,
        "n_repeated": 4,
        "class_sep": 0.75,
        "n_classes": 4,
    },
    "test_dataset_4": {
        "n_samples": 3000,
        "n_features": 25,
        "n_informative": 10,
        "n_redundant": 6,
        "n_repeated": 2,
        "class_sep": 0.8,
        "n_classes": 4,
    },
    "test_dataset_5": {
        "n_samples": 5000,
        "n_features": 25,
        "n_informative": 15,
        "n_redundant": 3,
        "n_repeated": 2,
        "class_sep": 0.7,
        "n_classes": 5,
        "n_clusters_per_class": 5,
        "flip_y": 0.2,
    },
    "test_dataset_6": {
        "n_samples": 6000,
        "n_features": 20,
        "n_informative": 15,
        "n_redundant": 2,
        "n_repeated": 3,
        "class_sep": 0.6,
        "n_classes": 5,
        "n_clusters_per_class": 5,
    },
    "test_dataset_7": {
        "n_samples": 7000,
        "n_features": 20,
        "n_informative": 15,
        "n_classes": 4,
        "n_clusters_per_class": 3,
    },
    "test_dataset_8": {
        "n_samples": 1000,
        "n_features": 35,
        "n_informative": 15,
        "n_classes": 4,
        "n_clusters_per_class": 3,
    },
    "test_dataset_9": {
        "n_samples": 800,
        "n_features": 30,
        "n_informative": 20,
        "n_classes": 3,
        "n_clusters_per_class": 3,
    },
    "test_dataset_10": {
        "n_samples": 500,
        "n_features": 40,
        "n_informative": 25,
        "n_classes": 3,
    },
    "test_dataset_11": {
        "n_samples": 300,
        "n_features": 10,
        "n_informative": 4,
        "class_sep": 0.9,
        "n_classes": 3,
        "flip_y": 0.001,
    },
    "test_dataset_11": {
        "n_samples": 500,
        "n_features": 12,
        "n_informative": 8,
        "n_redundant": 3,
        "class_sep": 1.0,
        "n_clusters_per_class": 3,
        "flip_y": 0.001,
    },
    "test_dataset_12": {
        "n_samples": 1000,
        "n_features": 14,
        "n_informative": 5,
        "n_redundant": 4,
        "n_repeated": 2,
        "class_sep": 0.5,
        "n_classes": 4,
        "flip_y": 0.001,
    },
    "test_dataset_13": {
        "n_samples": 2000,
        "n_features": 15,
        "n_informative": 3,
        "n_redundant": 3,
        "n_repeated": 4,
        "class_sep": 0.75,
        "n_classes": 4,
        "flip_y": 0.001,
    },
    "test_dataset_21": {
        "n_samples": 300,
        "n_features": 10,
        "n_informative": 4,
        "class_sep": 0.9,
        "n_classes": 3,
        "flip_y": 0,
    },
    "test_dataset_21": {
        "n_samples": 500,
        "n_features": 12,
        "n_informative": 8,
        "n_redundant": 3,
        "class_sep": 1.0,
        "n_clusters_per_class": 3,
        "flip_y": 0,
    },
    "test_dataset_22": {
        "n_samples": 1000,
        "n_features": 14,
        "n_informative": 5,
        "n_redundant": 4,
        "n_repeated": 2,
        "class_sep": 0.5,
        "n_classes": 4,
        "flip_y": 0,
    },
    "test_dataset_23": {
        "n_samples": 2000,
        "n_features": 15,
        "n_informative": 3,
        "n_redundant": 3,
        "n_repeated": 4,
        "class_sep": 0.75,
        "n_classes": 4,
        "flip_y": 0,
    },
    "test_dataset_31": {
        "n_samples": 300,
        "n_features": 10,
        "n_informative": 4,
        "class_sep": 0.01,
        "n_classes": 3,
        "flip_y": 0,
    },
    "test_dataset_31": {
        "n_samples": 500,
        "n_features": 12,
        "n_informative": 8,
        "n_redundant": 3,
        "class_sep": 0.01,
        "n_clusters_per_class": 3,
        "flip_y": 0,
    },
    "test_dataset_32": {
        "n_samples": 1000,
        "n_features": 14,
        "n_informative": 5,
        "n_redundant": 4,
        "n_repeated": 2,
        "class_sep": 0.01,
        "n_classes": 4,
        "flip_y": 0,
    },
    "test_dataset_33": {
        "n_samples": 2000,
        "n_features": 15,
        "n_informative": 3,
        "n_redundant": 3,
        "n_repeated": 4,
        "class_sep": 0.01,
        "n_classes": 4,
        "flip_y": 0,
    },
    "test_dataset_41": {
        "n_samples": 300,
        "n_features": 10,
        "n_informative": 8,
        "class_sep": 0.01,
        "n_classes": 3,
        "flip_y": 0,
    },
    "test_dataset_41": {
        "n_samples": 500,
        "n_features": 12,
        "n_informative": 9,
        "class_sep": 0.01,
        "n_clusters_per_class": 3,
        "flip_y": 0,
    },
    "test_dataset_42": {
        "n_samples": 1000,
        "n_features": 14,
        "n_informative": 9,
        "class_sep": 0.01,
        "n_classes": 4,
        "flip_y": 0,
    },
    "test_dataset_43": {
        "n_samples": 2000,
        "n_features": 15,
        "n_informative": 12,
        "class_sep": 0.01,
        "n_classes": 4,
        "flip_y": 0,
    },
    "test_dataset_51": {
        "n_samples": 300,
        "n_features": 10,
        "n_informative": 8,
        "class_sep": 0.01,
        "flip_y": 0,
    },
    "test_dataset_51": {
        "n_samples": 500,
        "n_features": 12,
        "n_informative": 9,
        "class_sep": 0.01,
        "flip_y": 0,
    },
    "test_dataset_52": {
        "n_samples": 1000,
        "n_features": 14,
        "n_informative": 9,
        "class_sep": 0.01,
        "flip_y": 0,
    },
    "test_dataset_53": {
        "n_samples": 2000,
        "n_features": 15,
        "n_informative": 12,
        "class_sep": 0.01,
        "flip_y": 0,
    },
    "test_dataset_61": {
        "n_samples": 300,
        "n_features": 5,
        "n_informative": 4,
        "class_sep": 0.01,
        "flip_y": 0,
    },
    "test_dataset_61": {
        "n_samples": 500,
        "n_features": 6,
        "n_informative": 4,
        "class_sep": 0.01,
        "flip_y": 0,
    },
    "test_dataset_62": {
        "n_samples": 1000,
        "n_features": 7,
        "n_informative": 4,
        "class_sep": 0.01,
        "flip_y": 0,
    },
    "test_dataset_63": {
        "n_samples": 2000,
        "n_features": 8,
        "n_informative": 5,
        "class_sep": 0.01,
        "flip_y": 0,
    },
    "test_dataset_70": {
        "n_samples": 300,
        "n_features": 5,
        "n_informative": 4,
        "n_redundant": 0,
        "n_repeated": 0,
        "class_sep": 1,
        "flip_y": 0,
    },
    "test_dataset_71": {
        "n_samples": 500,
        "n_features": 6,
        "n_informative": 5,
        "n_redundant": 0,
        "n_repeated": 0,
        "class_sep": 1,
        "flip_y": 0,
    },
    "test_dataset_72": {
        "n_samples": 1000,
        "n_features": 7,
        "n_informative": 6,
        "n_redundant": 0,
        "n_repeated": 0,
        "class_sep": 1,
        "flip_y": 0,
    },
    "test_dataset_73": {
        "n_samples": 2000,
        "n_features": 8,
        "n_informative": 7,
        "n_redundant": 0,
        "n_repeated": 0,
        "class_sep": 1,
        "flip_y": 0,
    },
    "test_dataset_80": {
        "n_samples": 300,
        "n_features": 5,
        "n_informative": 4,
        "n_redundant": 0,
        "n_repeated": 0,
        "class_sep": 2,
        "flip_y": 0,
    },
    "test_dataset_81": {
        "n_samples": 500,
        "n_features": 6,
        "n_informative": 5,
        "n_redundant": 0,
        "n_repeated": 0,
        "class_sep": 2,
        "flip_y": 0,
    },
    "test_dataset_82": {
        "n_samples": 1000,
        "n_features": 7,
        "n_informative": 6,
        "n_redundant": 0,
        "n_repeated": 0,
        "class_sep": 2,
        "flip_y": 0,
    },
    "test_dataset_83": {
        "n_samples": 2000,
        "n_features": 8,
        "n_informative": 7,
        "n_redundant": 0,
        "n_repeated": 0,
        "class_sep": 2,
        "flip_y": 0,
    },
    "test_dataset_90": {
        "n_samples": 300,
        "n_features": 15,
        "n_informative": 9,
        "n_redundant": 1,
        "n_repeated": 1,
        "class_sep": 2,
        "flip_y": 0.1,
    },
    "test_dataset_91": {
        "n_samples": 500,
        "n_features": 16,
        "n_informative": 12,
        "n_redundant": 1,
        "n_repeated": 1,
        "class_sep": 2,
        "flip_y": 0.1,
    },
    "test_dataset_92": {
        "n_samples": 1000,
        "n_features": 17,
        "n_informative": 12,
        "n_redundant": 1,
        "n_repeated": 1,
        "class_sep": 2,
        "flip_y": 0.1,
    },
    "test_dataset_93": {
        "n_samples": 2000,
        "n_features": 18,
        "n_informative": 12,
        "n_redundant": 1,
        "n_repeated": 1,
        "class_sep": 2,
        "flip_y": 0.1,
    },
}
"""

dataset_dict = {
    "test_dataset_0": {
        "n_samples": 300,
        "n_features": 10,
        "n_informative": 4,
        "class_sep": 0.9,
        "n_classes": 3,
        "flip_y": 0.3,
    },
    "test_dataset_1": {
        "n_samples": 500,
        "n_features": 12,
        "n_informative": 8,
        "n_redundant": 3,
        "class_sep": 1.0,
        "n_clusters_per_class": 3,
        "flip_y": 0.1,
    },
    "test_dataset_2": {
        "n_samples": 1000,
        "n_features": 14,
        "n_informative": 5,
        "n_redundant": 4,
        "n_repeated": 2,
        "class_sep": 0.5,
        "n_classes": 4,
        "flip_y": 0.1,
    },
}
