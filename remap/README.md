# Windows Virtual Desktop Manager (AutoHotkey v2)

A productivity-enhancing AutoHotkey v2 script that:
- Switches between Windows virtual desktops using `Alt + 1` to `Alt + 4`
- Hides the taskbar automatically
- Refocuses windows reliably using an Alt+Tab trick
- Provides Vim-style navigation with `Alt + H/J/K/L`
- Automatically restores focus to windows after switching

---

## 🚀 Features

- 🔢 **Switch Desktops:** `Alt + 1` to `Alt + 4`
- 🧼 **Hide Taskbar Automatically**
- 🎯 **Auto-Focus Active Window** after switch
- 🧭 **Vim-style Movement:** `Alt + H/J/K/L` (← ↓ ↑ →)

---

## 📁 Requirements

- Windows 10 or 11
- [AutoHotkey v2](https://www.autohotkey.com/)
- `VirtualDesktopAccessor.dll` (must be in the same folder as the script)

---

## 🔧 Setup Instructions

1. **Install AutoHotkey v2**
   - Download and install from [https://www.autohotkey.com/](https://www.autohotkey.com/)

2. **Download VirtualDesktopAccessor.dll**
   - From [GitHub Releases](https://github.com/Ciantic/VirtualDesktopAccessor/releases)
   - Place the DLL in the same folder as your script

3. **Save the Script**
   - Name it `virtual_desktops.ahk` or any name you like

4. **Run the Script**
   - Double-click the `.ahk` file to run

---

## 🖥️ Auto Start on Boot

To run the script when Windows starts:

1. Press `Win + R`, type: `shell:startup`

---

## 📜 Hotkeys Summary

| Hotkey        | Action                          |
|---------------|----------------------------------|
| `Alt + 1`     | Switch to Desktop 1             |
| `Alt + 2`     | Switch to Desktop 2             |
| `Alt + 3`     | Switch to Desktop 3             |
| `Alt + 4`     | Switch to Desktop 4             |
| `Alt + H/J/K/L` | Vim-style Arrow Navigation   |

---


## 📄 License

MIT License. Use freely and modify for personal productivity.

---

## 🤝 Credits

- [`VirtualDesktopAccessor`](https://github.com/Ciantic/VirtualDesktopAccessor) by Ciantic
- AutoHotkey community for scripting support
