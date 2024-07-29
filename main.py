import speech_recognizer as sr
import os

fs = 44100
duration = 3
filename = "output.wav"

print("Welcome to the Voice Assistant!")

while True:
    prompt = input("What app would like to open?\nCalculator\nTextEdit\nZoom\nTerminal\n\n"
                   "To start recording enter 'R' to quit press 'Q'")
    if prompt == "R":
        sr.record_audio(filename, duration, fs)
        speech = sr.recognize_speech_from_audio(filename).capitalize()

        if speech == "Calculator":
            os.system("open -a Calculator")
        elif speech == "Text edit":
            os.system("open -a TextEdit")
        elif speech == "Zoom":
            os.system("open -a zoom.us")
        elif speech == "Terminal":
            os.system("open -a Terminal")
