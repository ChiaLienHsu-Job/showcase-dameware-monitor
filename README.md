Showcase - DameWare Monitor

A small Python + Qt tool that monitors DameWare Mini Remote Control
(DWRCS.exe) connections.
If a remote user connects to the DameWare service (default TCP port
6129), the app will immediately show a warning dialog.

This project is a showcase/demo project to demonstrate: - System
monitoring using psutil - GUI alerts using PySide6 (Qt for Python) -
Security awareness by detecting suspicious remote connections

------------------------------------------------------------------------

✨ Features

-   Detects if DWRCS.exe has active ESTABLISHED connections
-   Filters out local loopback connections (127.0.0.1 / ::1) to avoid
    false positives
-   Shows a Qt warning popup when a remote session is detected
-   Logs remote IP and timestamp (optional extension)

------------------------------------------------------------------------

🛠 Requirements

-   Python 3.11 (recommended)
-   Packages:
    -   psutil
    -   PySide6

Install all dependencies:

    pip install -r requirements.txt

------------------------------------------------------------------------

🚀 Usage

Run the monitor:

    python dameware_monitor.py

When a remote session is established, a warning popup will appear:

[warning-sample]

(screenshot placeholder – replace with your actual image)

------------------------------------------------------------------------

📦 Build Executable (Optional)

If you want to create a standalone .exe (no Python required):

1.  Install PyInstaller

        pip install pyinstaller

2.  Build executable

        pyinstaller --onefile --noconsole dameware_monitor.py

3.  The .exe will be in the dist/ folder.

------------------------------------------------------------------------

📂 Project Structure

    showcase-dameware-monitor/
    │
    ├─ dameware_monitor.py     # main program
    ├─ requirements.txt        # dependencies
    ├─ README.md               # documentation
    └─ .gitignore              # ignore venv, build files

------------------------------------------------------------------------

📜 License

MIT License – feel free to use and modify for personal or educational
purposes.
