
from methods import GoogleAdapter, SphinxAdapter

from settings import get_fullpath


if __name__ == "__main__":
    files = [
        ("early_short_stories_0001.wav", "kaggle"),
        ("early_short_stories_0002.wav", "kaggle"),
        ("early_short_stories_0003.wav", "kaggle"),
        ("early_short_stories_0004.wav", "kaggle"),
        ("early_short_stories_0005.wav", "kaggle"),
        ("decoder-test.wav", None),
        ("machine-short.wav", None),
        ("machine.wav", None),
        ("russian-short.wav", None),
        ("russian.wav", None),
    ]

    for filename, directory in files:
        filename = get_fullpath(filename, directory=directory)
        try:
            google_text = GoogleAdapter().speech_to_text(filename)
        except:
            google_text = "No"
        sphinx_text = SphinxAdapter().speech_to_text(filename)
        print(google_text)
        print(sphinx_text)
