import subprocess
import sys
from pathlib import Path

def run():
    app_path = Path(__file__).parent / "ui.py"
    subprocess.run([sys.executable, "-m", "streamlit", "run", str(app_path)])