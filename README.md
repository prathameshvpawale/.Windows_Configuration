# My Virtual Desktop Script

This script is for my personal Windows desktop setup.

## 🔧 What it does:

- `Alt + 1` → Switch to Desktop 1  
- `Alt + 2` → Switch to Desktop 2  
- `Alt + 3` → Switch to Desktop 3  
- `Alt + 4` → Switch to Desktop 4  
- `Alt + H/J/K/L` → Move cursor left/down/up/right (Vim-style keys)

When switching desktops:
- Taskbar is automatically hidden
- Active window is auto-focused using an Alt+Tab trick

## 🐍 Python Automation (My Setup)

I use Python scripts to automatically launch and move apps to specific virtual desktops.

### Example Use Cases:
- Launch browser on Desktop 1  
- Start terminal on desktop 2
- Open terminal on Desktop 3  
- Focus specific tasks on separate desktops

These Python scripts work together with this AutoHotkey script using:
- `subprocess` to launch apps
- `VirtualDesktopAccessor.dll` for desktop control

> Python scripts are in my `automation/` folder

---

## 📁 Requirements:

- AutoHotkey v2  
- `VirtualDesktopAccessor.dll` (must be in the same folder)  
- Python (`pyautogui`) for automation

---

## 🧠 Notes:

This is a private setup to boost my daily workflow using virtual desktops.
