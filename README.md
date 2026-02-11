## 3CX Spotify Pauser (Windows)

A lightweight Windows utility that instantly pauses Spotify when executed.
Built in Python and packaged as a single EXE using PyInstaller.

Uses Windows System Media Transport Controls (SMTC) — the same native API Windows uses for media playback control.

✅ Features

True pause (not mute)

Works while Spotify is in the background

No media key injection

No AutoHotkey

No internet connection required

No Spotify API / OAuth

Silent execution (no console window)

Single portable executable

🖥 Requirements (for building)

Windows 10 or Windows 11

Python 3.9+

Spotify desktop app (web player not supported)

📦 Install dependencies

Dependencies are listed in requirements.txt.

pip install -r requirements.txt

▶ Usage (Python)
python main.py


Spotify will pause immediately if it is running and playing.

🛠 Build EXE
pyinstaller --onefile --noconsole --icon=spotify.ico --hidden-import=winrt.windows.media.control --hidden-import=winrt.windows.foundation main.py

📁 Output

The compiled executable will be created at:

dist\3CX-Spotify-Pauser.exe


(Double-click to pause Spotify to test.)
Set it as the executable file to be ran when you recieve an incoming call in 3CX in the settings.

ℹ Notes

Spotify must be running to be detected

If multiple media sessions exist, Spotify will be paused specifically

Behaviour matches Windows’ native media controls

Designed to be used as a one-click utility (e.g. before calls)

📄 License

MIT License
