#!/usr/bin/env python3
import pyaudio
from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave


CHANNELS = 2
RATE = 44100
CHUNK = 4096
FORMAT = pyaudio.paInt16


model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
#sample_size = pyaudio.get_sample_size(FORMAT)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())