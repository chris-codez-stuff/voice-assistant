import time
from gtts import gTTS
from pydub import AudioSegment
import pygame


def text_to_audio(text):
    language = "en"

    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")


def play():
    try:
        pygame.mixer.quit()  # Reset state
        pygame.mixer.init()
        print(f"Loading output.mp3")
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(1)

        print("Audio played successfully.")

    except Exception as e:
        print(f"Error in play: {e}")


if __name__ == "__main__":
    text_to_audio("Talking computer is very cool")
    play()
