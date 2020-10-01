from abc import ABCMeta, abstractmethod

from speech_recognition import AudioFile, Recognizer

from settings import get_fullpath


class SpeechRecognitionMethod:
    def __init__(self, filename):
        self.__filename = filename

    def recognize_google(self):
        audio = AudioFile(self.__filename)
        recognizer = Recognizer()

        with audio as audio_file:
            audio_content = recognizer.record(audio_file)
            result = recognizer.recognize_google(audio_content, language="ru-RU")

        return result

    def recognize_sphinx(self):
        audio = AudioFile(self.__filename)
        recognizer = Recognizer()

        with audio as audio_file:
            audio_content = recognizer.record(audio_file)
            result = recognizer.recognize_sphinx(audio_content, language="ru-RU")

        return result


class YandexSpeechMethod:
    def __init__(self):
        pass

    def recognize(self):
        pass


class KaldiSpeechMethod:
    def __init__(self):
        pass

    def recognize(self):
        pass


class Adapter(metaclass=ABCMeta):
    @abstractmethod
    def speech_to_text(self, filename):
        pass


class GoogleAdapter(Adapter):
    def speech_to_text(self, filename):
        method = SpeechRecognitionMethod(filename)
        return method.recognize_google()


class SphinxAdapter(Adapter):
    def speech_to_text(self, filename):
        method = SpeechRecognitionMethod(filename)
        return method.recognize_sphinx()


class YandexAdapter(Adapter):
    def speech_to_text(self, filename):
        method = YandexSpeechMethod(filename)
        return method.recognize()


class KaldiAdapter(Adapter):
    def speech_to_text(self, filename):
        method = KaldiSpeechMethod(filename)
        return method.recognize()
