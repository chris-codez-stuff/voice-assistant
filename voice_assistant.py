import tkinter as tk
from tkinter import messagebox
import os
import speech_recognizer as sr

commands = {
    "open calculator": "open -a Calculator",
    "open text edit": "open -a TextEdit",
    "open zoom": "open -a zoom.us",
    "open terminal": "open -a Terminal"
}


def start_recording():
    fs = 44100
    duration = int(duration_entry.get())
    filename = "output.wav"

    sr.record_audio(filename, duration, fs)
    speech = sr.recognize_speech_from_audio(filename).lower()

    if speech:
        recognized_command_label.config(text=f"Recognized Command: {speech}")
        if speech in commands:
            os.system(commands[speech])
            log_action(f"Executed: {speech}")
        else:
            messagebox.showerror("Error", "Sorry, I could not recognize the command.")
            log_action(f"Failed to recognize: {speech}")
    else:
        recognized_command_label.config(text="Could not recognize any command")
        log_action("Failed to recognize any command")


def update_commands_label():
    commands_text = "Available Commands:\n" + "\n".join([f"- {cmd}" for cmd in commands.keys()])
    commands_label.config(text=commands_text)


def log_action(action):
    history_listbox.insert(tk.END, action)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


root = tk.Tk()
root.title("Voice Assistant")
root.geometry("400x500")

label = tk.Label(root, text="Voice Assistant", font=("Helvetica", 16))
label.pack(pady=10)

commands_label = tk.Label(root, text="", font=("Helvetica", 12))
commands_label.pack(pady=10)
update_commands_label()

duration_label = tk.Label(root, text="Recording Duration (seconds):", font=("Helvetica", 12))
duration_label.pack(pady=5)
duration_entry = tk.Entry(root, font=("Helvetica", 12))
duration_entry.insert(0, "3")
duration_entry.pack(pady=5)

record_button = tk.Button(root, text="Start Recording", command=start_recording, font=("Helvetica", 14))
record_button.pack(pady=20)

recognized_command_label = tk.Label(root, text="", font=("Helvetica", 12))
recognized_command_label.pack(pady=10)

history_label = tk.Label(root, text="Command History:", font=("Helvetica", 12))
history_label.pack(pady=5)
history_listbox = tk.Listbox(root, font=("Helvetica", 12), height=10, width=50)
history_listbox.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=on_closing, font=("Helvetica", 14))
exit_button.pack(pady=20)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
