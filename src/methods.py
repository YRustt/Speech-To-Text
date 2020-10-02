from abc import ABCMeta, abstractmethod

from speech_recognition import AudioFile, Recognizer, UnknownValueError


class SpeechRecognitionMethod:
    def __init__(self, filename, duration=None):
        self.__filename = filename
        self.__duration = duration

    def __recognize(self, method):
        audio = AudioFile(self.__filename)
        recognizer = Recognizer()

        with audio as audio_file:
            result_text = []
            try:
                while True:
                    audio_content = recognizer.record(audio_file, duration=self.__duration)
                    text = getattr(recognizer, method)(audio_content, language="ru-RU")
                    result_text.append(text)
            except UnknownValueError as er:
                print("End", er)

        return " ".join(result_text)

    def recognize_google(self):
        return self.__recognize("recognize_google")

    def recognize_sphinx(self):
        return self.__recognize("recognize_sphinx")


class YandexSpeechMethod:
    def __init__(self):
        pass

    def recognize(self):
        raise NotImplementedError()


class KaldiSpeechMethod:
    def __init__(self):
        pass

    def recognize(self):
        raise NotImplementedError()


class Adapter(metaclass=ABCMeta):
    @abstractmethod
    def speech_to_text(self, filename):
        pass


class GoogleAdapter(Adapter):
    def speech_to_text(self, filename, duration=None):
        method = SpeechRecognitionMethod(filename, duration)
        return method.recognize_google()


class SphinxAdapter(Adapter):
    def speech_to_text(self, filename, duration=None):
        method = SpeechRecognitionMethod(filename, duration)
        return method.recognize_sphinx()


class YandexAdapter(Adapter):
    def speech_to_text(self, filename):
        method = YandexSpeechMethod(filename)
        return method.recognize()


class KaldiAdapter(Adapter):
    def speech_to_text(self, filename):
        method = KaldiSpeechMethod(filename)
        return method.recognize()
