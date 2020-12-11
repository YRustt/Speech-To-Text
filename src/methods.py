import os
import wave
from abc import ABCMeta, abstractmethod

from speech_recognition import AudioFile, Recognizer, UnknownValueError
from google.cloud import speech

from settings import CREDENTIALS_FILE


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
    def __init__(self, filename):
        pass

    def recognize(self):
        raise NotImplementedError()


class KaldiSpeechMethod:
    def __init__(self, filename):
        pass

    def recognize(self):
        raise NotImplementedError()


class GoogleCloudSpeechMethod:
    CREDENTIALS_VAR = "GOOGLE_APPLICATION_CREDENTIALS"

    def __init__(self, filename):
        self.__filename = filename

        os.environ[self.CREDENTIALS_VAR] = CREDENTIALS_FILE
        self.__client = speech.SpeechClient()

    def __get_audio(self):
        with wave.open(self.__filename, "rb") as file:
            audio_channel_count = file.getnchannels()
            sample_rate_herts = file.getframerate()
            content = file.readframes(file.getnframes())
            audio = speech.RecognitionAudio(content=content)

        return audio, audio_channel_count, sample_rate_herts

    def recognize(self):
        audio, audio_channel_count, sample_rate_herts = self.__get_audio()
        config = speech.RecognitionConfig(
            language_code="ru-RU",
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=sample_rate_herts,
            audio_channel_count=audio_channel_count
        )
        response = self.__client.recognize(config=config, audio=audio)

        print(response.results)
        return response.results[0].alternatives[0].transcript

    def __del__(self):
        self.__client = None
        del os.environ[self.CREDENTIALS_VAR]


class Adapter(metaclass=ABCMeta):
    @abstractmethod
    def speech_to_text(self, filename, duration=None):
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
    def speech_to_text(self, filename, duration=None):
        method = YandexSpeechMethod(filename)
        return method.recognize()


class KaldiAdapter(Adapter):
    def speech_to_text(self, filename, duration=None):
        method = KaldiSpeechMethod(filename)
        return method.recognize()


class GoogleCloudAdapter(Adapter):
    def speech_to_text(self, filename, duration=None):
        method = GoogleCloudSpeechMethod(filename)
        return method.recognize()
