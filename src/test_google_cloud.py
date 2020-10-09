import io
import os
import sys

# Imports the Google Cloud client library
from google.cloud import speech


# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
# file_name = "../dataset/videoregistrator.flac"

# Loads the audio into memory
# with io.open(file_name, "rb") as audio_file:
#     content = audio_file.read()
#     audio = speech.RecognitionAudio(content=content)

audio = speech.RecognitionAudio(uri=sys.argv[1])

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz=44100,
    language_code="ru-RU",
    audio_channel_count=2
)

# Detects speech in the audio file
operation = client.long_running_recognize(request={"config": config, "audio": audio})

print("Waiting for operation to complete...")
response = operation.result(timeout=200)

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
