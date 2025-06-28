# 🎬 YouTube Downloader (GUI)

A simple and powerful **desktop app** for downloading YouTube videos and playlists — built with **Python**, **Tkinter**, and **yt-dlp**.  
No coding needed, just paste the link and download! 🔽

---

## ✨ Features

- ✅ Download **YouTube videos** and **playlists**
- ✅ Choose quality: `Best`, `1080p`, `720p`, or `Audio Only`
- ✅ Save videos to your selected folder
- ✅ Shows real-time **download progress**
- ✅ Outputs final video in `.mp4` (no `.webm`)
- ✅ Comes with `ffmpeg` built-in — **no extra install needed**
- ✅ No terminal popups — clean GUI only

---

## 📸 Screenshot

> _(Add a screenshot named `screenshot.png` if you want visual preview)_

---

## 📦 Download the App

🖱️ [Click here to download the latest release](https://github.com/your-username/your-repo-name/releases)

- Unzip the file
- Run `main.exe`
- Paste a YouTube URL and hit **Download**

⚠️ No need to install Python or ffmpeg. Just run and enjoy!

---

## 🛠️ Run from Source (For Developers)

### ✅ Requirements

- Python 3.7+
- `yt-dlp` (Python wrapper for YouTube downloads)
- `ffmpeg.exe` in the project directory

### 🔧 Setup

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
python main.py
````

---

## 🔨 Build the `.exe` Yourself

### 1. Place `ffmpeg.exe` in the root folder

> Download from: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

### 2. Run the `build.bat` file (included)

```bash
build.bat
```

### 3. Done! `main.exe` will be inside the `dist/` folder.

> ✅ `ffmpeg` is bundled into the `.exe` using PyInstaller’s `--add-data`.

---

## 🧱 Folder Structure

```
youtube-downloader-gui/
├── main.py
├── ffmpeg.exe
├── build.bat
├── README.md
├── requirements.txt
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

* Thumbnail preview
* Multi-download queue
* Dark mode UI

Let’s build it together! 🛠️

---

## 📜 License

This project is open-source and licensed under the [MIT License](LICENSE).

---

## 📝 What You Need to Do:

1. Replace:
   - `your-username/your-repo-name` with your actual GitHub link
2. Add:
   - `screenshot.png` (optional)
   - `requirements.txt` with:
     ```txt
     yt-dlp
     ```

3. Add a `LICENSE` file (MIT is good — I can generate one for you too)


