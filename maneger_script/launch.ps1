# --- PowerShell Script to Launch a Python Script in a Virtual Environment ---

# Path to the virtual environment's activate script::venv\Scripts\Activate.ps1
$venvActivate = "..."

# Path to the Python script :::main.py
$pythonScript = "..."

# Run the activation and script directly
. "$venvActivate"
python "$pythonScript"



