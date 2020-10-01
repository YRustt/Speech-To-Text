import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
DATASET_DIR = os.path.join(ROOT_DIR, "dataset")


def get_fullpath(filename, *, directory=None):
    if directory is not None:
        return os.path.join(DATASET_DIR, directory, filename)
    else:
        return os.path.join(DATASET_DIR, filename)
