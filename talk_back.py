import time
from gtts import gTTS
from pydub import AudioSegment
import pygame


def text_to_audio(text):
    language = "en"

    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")

    audio = AudioSegment.from_mp3("output.mp3")
    audio.export("output.wav", format="wav")


def play():
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

    print("Conversion completed and audio played successfully.")


if __name__ == "__main__":
    text_to_audio("Talking computer")
    play()
