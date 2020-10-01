
from methods import GoogleAdapter, SphinxAdapter

from settings import get_fullpath


if __name__ == "__main__":
    filename = get_fullpath("machine-short-low-sample-rate.wav")
    print(GoogleAdapter().speech_to_text(filename))
    print(SphinxAdapter().speech_to_text(filename))
