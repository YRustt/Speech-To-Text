from logmmse import logmmse_from_file

from settings import get_denoise_filename


def denoise(filename, output_filename):
    """Функция для удаления шума из wav-файла.
    
    Args:
        filename (str): путь к wav-файлу.
        output_filename: путь к wav-файлу с результатом удаления шума.

    Returns:
        None
    """

    logmmse_from_file(filename, output_filename, initial_noise=10, window_size=0, noise_threshold=0.3)
