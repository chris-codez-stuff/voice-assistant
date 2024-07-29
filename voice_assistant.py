import tkinter as tk
from tkinter import messagebox
import os
import speech_recognizer as sr


def start_recording():
    fs = 44100
    duration = 3
    filename = "output.wav"

    sr.record_audio(filename, duration, fs)
    speech = sr.recognize_speech_from_audio(filename).lower()

    if speech == "open calculator":
        os.system("open -a Calculator")
    elif speech == "open text edit":
        os.system("open -a TextEdit")
    elif speech == "open zoom":
        os.system("open -a zoom.us")
    elif speech == "open terminal":
        os.system("open -a Terminal")
    else:
        messagebox.showerror("Error", "Sorry, I could not recognize the command.")


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


root = tk.Tk()
root.title("Voice Assistant")
root.geometry("300x300")

label = tk.Label(root, text="Voice Assistant", font=("Helvetica", 16))
label.pack(pady=10)

commands_label = tk.Label(root,
                          text="Available Commands:\n- Open calculator\n- Open TextEdit\n- Open Zoom\n- Open Terminal",
                          font=("Helvetica", 12))
commands_label.pack(pady=10)

record_button = tk.Button(root, text="Start Recording", command=start_recording, font=("Helvetica", 14))
record_button.pack(pady=20)

exit_button = tk.Button(root, text="Exit", command=on_closing, font=("Helvetica", 14))
exit_button.pack(pady=20)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
