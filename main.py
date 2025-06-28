import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from yt_dlp import YoutubeDL
import threading
import os
import sys

# ---------- Helper: Get ffmpeg path ----------
def get_ffmpeg_path():
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, 'ffmpeg.exe')
    else:
        return os.path.join(os.getcwd(), 'ffmpeg.exe')

# ---------- GUI Functions ----------
def browse_directory():
    folder = filedialog.askdirectory()
    if folder:
        output_path.set(folder)

def start_download():
    threading.Thread(target=download_video).start()

def progress_hook(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded_bytes = d.get('downloaded_bytes', 0)
        if total_bytes:
            percent = downloaded_bytes / total_bytes * 100
            progress_bar['value'] = percent
            status_label.config(text=f"Downloading... {percent:.2f}%")
    elif d['status'] == 'finished':
        status_label.config(text="✅ Download complete!")

def download_video():
    url = url_entry.get().strip()
    path = output_path.get().strip()
    quality = format_choice.get()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    if not path:
        messagebox.showerror("Error", "Please select a download folder")
        return

    progress_bar['value'] = 0
    status_label.config(text="Starting...")

    format_map = {
        "Best": "bestvideo+bestaudio/best",
        "1080p": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
        "720p": "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "Audio Only": "bestaudio"
    }

    ffmpeg_path = get_ffmpeg_path()

    ydl_opts = {
        'format': format_map.get(quality, "best"),
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
        'quiet': True,
        'noplaylist': False,
        'ffmpeg_location': ffmpeg_path,
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }]
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download completed!")
    except Exception as e:
        status_label.config(text="❌ Download failed.")
        messagebox.showerror("Error", str(e))

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("🎬 YouTube Downloader")
root.geometry("600x350")
root.resizable(False, False)

tk.Label(root, text="YouTube Video or Playlist URL:", font=('Arial', 10)).pack(pady=5)
url_entry = tk.Entry(root, width=70)
url_entry.pack()

tk.Label(root, text="Select Output Folder:", font=('Arial', 10)).pack(pady=5)
path_frame = tk.Frame(root)
path_frame.pack()

output_path = tk.StringVar()
tk.Entry(path_frame, textvariable=output_path, width=50).pack(side=tk.LEFT)
tk.Button(path_frame, text="Browse", command=browse_directory).pack(side=tk.LEFT)

tk.Label(root, text="Choose Quality/Format:", font=('Arial', 10)).pack(pady=5)
format_choice = ttk.Combobox(root, values=["Best", "1080p", "720p", "Audio Only"], state="readonly")
format_choice.set("Best")
format_choice.pack()

tk.Button(root, text="⬇ Download", font=('Arial', 12), command=start_download).pack(pady=15)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
progress_bar.pack(pady=5)

status_label = tk.Label(root, text="", fg="green", font=('Arial', 10, "italic"))
status_label.pack()

root.mainloop()
