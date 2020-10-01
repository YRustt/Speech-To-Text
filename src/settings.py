import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
DATASET_DIR = os.path.join(ROOT_DIR, "dataset")


def get_fullpath(filename, *, directory=None):
    """Функция для получения абсолютного пути к wav-файлу."""

    if directory is not None:
        return os.path.join(DATASET_DIR, directory, filename)
    else:
        return os.path.join(DATASET_DIR, filename)


def get_denoise_filename(filename):
    """Функция для получения пути к wav-файлу без шума."""

    path, name = os.path.split(filename)
    name, ext = name.split(".")
    output_name = f"{name}-denoise.{ext}"
    return os.path.join(path, output_name)
