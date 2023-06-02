"""Dataset information and manipulation"""
import pathlib


DATASETS_DIRNAME = ".datasets"

# A single variable that can be used to resolve a common known directory for datasets
# Default verson takes the form of {project_root}/.datasets (calculated relative to this module)
datasets_path = (
    pathlib.Path(__file__)
    .parent  # core
    .parent  # src
    .parent  # {workspace}
) / DATASETS_DIRNAME
