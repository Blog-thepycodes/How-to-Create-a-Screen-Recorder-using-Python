import tkinter as tk
import pyscreenrec # Make sure you have the necessary library installed
 
 
# Create the main application window
root = tk.Tk()
root.geometry("400x500")
root.title("Custom Screen Recorder - The Pycodes")
root.config(bg="black")
root.resizable(False, False)
 
 
# Title label
title_label = tk.Label(root, text="Custom Screen Recorder", font="arial 20 bold", bg="black", fg="red")
title_label.place(x=40, y=100)
 
 
# Initialize the screen recorder
recorder = pyscreenrec.ScreenRecorder()
 
 
# Function to start recording
def start_recording():
    filename = filename_entry.get()
    recorder.start_recording(str(filename + ".mp4"), 5)
 
 
# Function to pause recording
def pause_recording():
    recorder.pause_recording()
 
 
# Function to resume recording
def resume_recording():
    recorder.resume_recording()
 
 
# Function to stop recording
def stop_recording():
    recorder.stop_recording()
 
 
# Entry field for filename
filename = tk.StringVar()
filename_entry = tk.Entry(root, textvariable=filename, width=18, font="arial 15")
filename_entry.place(x=100, y=300)
filename.set("Name This Recording")
 
 
# Buttons for controlling recording
start_button = tk.Button(root, text="Start", font="arial 22", bg="black", fg="white", bd=0, command=start_recording)
start_button.place(x=155, y=200)
 
 
pause_button = tk.Button(root, text="Pause", font="arial 22", bg="black", fg="white", bd=0, command=pause_recording)
pause_button.place(x=50, y=400)
 
 
resume_button = tk.Button(root, text="Resume", font="arial 22", bg="black", fg="white", bd=0, command=resume_recording)
resume_button.place(x=150, y=400)
 
 
stop_button = tk.Button(root, text="Stop", font="arial 22", bg="black", fg="white", bd=0, command=stop_recording)
stop_button.place(x=269, y=400)
 
 
# Start the Tkinter main loop
root.mainloop()
