import tkinter as tk
from tkinter import messagebox
import threading
from pytube import YouTube
import random


def change_color():
    new_color = random_color()
    url_label.config(bg=new_color)
    root.after(1000, change_color) 

def random_color():
    return f"#{random.randint(0, 255):02X}{random.randint(0, 255):02X}{random.randint(0, 255):02X}"

def musICA():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL.")
        return
    try:
        yt = YouTube(url)
        stream = yt.streams.get_audio_only()
        download_thread = threading.Thread(target=start_download_audio, args=(yt.title, stream))
        stream.download()
        download_thread.start()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
def start_download_audio(video_title, stream):
    download_button.config(state=tk.DISABLED)
    download_label.config(text=f"Downloading: {video_title}")
    stream.download()
    messagebox.showinfo("Download Complete", f"Audio '{video_title}' downloaded successfully! ")
    download_label.config(text="")
    download_button.config(state=tk.NORMAL)

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL.")
        return
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()        
        download_thread = threading.Thread(target=start_download_video, args=(yt.title, stream))
        stream.download()
        download_thread.start()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def start_download_video(video_title, stream):
    download_button.config(state=tk.DISABLED)
    download_label.config(text=f"Downloading: {video_title}")
    stream.download()
    messagebox.showinfo("Download Complete", f"Video '{video_title}' downloaded successfully! ")

    download_label.config(text="")
    download_button.config(state=tk.NORMAL)


root = tk.Tk()
root.title("Mp3/Mp4 Play")



url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack()

url_entry = tk.Entry(root, width=40)
url_entry.pack()
canvas = tk.Canvas(root, width=400, height=100)
canvas.pack()

download_label = tk.Label(root, text="", font=("Helvetica", 12))
download_label.pack()
download_button = tk.Button(root, text="Video", command=download_video)
download_button.pack()
download_audio = tk.Button(root, text="Audio", command=musICA)
download_audio.pack()


change_color()
root.mainloop()





