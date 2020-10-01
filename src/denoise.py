from logmmse import logmmse_from_file

from settings import get_denoise_filename


def denoise(filename, output_filename):
    logmmse_from_file(filename, output_filename=output_filename)
