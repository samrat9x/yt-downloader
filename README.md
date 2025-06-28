# 🎬 YouTube Downloader (GUI)

A simple **desktop app** for downloading YouTube videos and playlists — built with **Python**, **Tkinter**, **yt-dlp** and **ffmpeg**.

---

## ✨ Features

- ✅ Download **YouTube videos** and **playlists**
- ✅ Choose quality: `Best`, `1080p`, `720p`, or `Audio Only`
- ✅ Save videos to your selected folder
- ✅ Shows real-time **download progress**
- ✅ Outputs final video in `.mp4`
- ✅ Comes with `ffmpeg` built-in — **no extra install needed**
- ✅ No terminal popups — clean GUI only

---

### ✅ Requirements

- Python 3.7+
- `yt-dlp` (Python wrapper for YouTube downloads)
- `ffmpeg.exe` in the project directory

---

## 🔨 Build the `.exe` Yourself

### 1. Clone the repo:

```bash
git clone https://github.com/samrat9x/yt-downloader
```

### 2. Install `yt-dlp`:

```bash
pip install yt-dlp
```

### 3. Install `pyinstaller`:

```bash
pip install pyinstaller
```

### 4. Download `ffmpeg.exe` and place it to the root folder

> Download from: [https://www.gyan.dev/ffmpeg/builds/](https://ffmpeg.org/download.html)

### 5. Open CMD in the root folder and run the following command:

```bash
pyinstaller --onefile --windowed --add-data "ffmpeg.exe;." main.py
```

### 6. You will find `main.exe` in the `dist` folder.

---

## 🧱 Folder Structure

```
yt-downloader/
├── main.py
├── ffmpeg.exe
├── README.md
└── dist/
    └── main.exe
```

---

## 🤝 Contribute

Pull requests welcome! 🙌

1. Fork this repo
2. Create a branch: `git checkout -b my-feature`
3. Make your changes
4. Push and submit a PR

Want to add features like:

- Thumbnail preview
- Multi-download queue
- Dark mode UI

Let’s build it together! 🛠️
