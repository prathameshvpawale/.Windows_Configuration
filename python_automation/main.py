import pyautogui
import time

pyautogui.PAUSE = 0.5  # Global delay after each PyAutoGUI call
pyautogui.FAILSAFE = True  # Move mouse to top-left to abort script

def close_extra_desktops(max_desktops=5):
    for _ in range(max_desktops):
        pyautogui.hotkey('win', 'ctrl', 'right')  # move to the next desktop

        pyautogui.hotkey('win', 'ctrl', 'f4')     # close current desktop

def switch_desktop_1(max_desktops=4):
    for _ in range(max_desktops):
        pyautogui.hotkey('win', 'ctrl', 'Left')  # move to the previes desktop

def open_run_box():
    pyautogui.hotkey('win', 'r')
    time.sleep(0.7)

def type_and_enter(command):
    pyautogui.typewrite(command)
    pyautogui.press('enter')
    time.sleep(2)
    #pyautogui.press('f11')  # Fullscreen

def create_new_desktop():
    pyautogui.hotkey('win', 'ctrl', 'd')


def switch_desktop_right():
    pyautogui.hotkey('win', 'ctrl', 'right')


def open_terminal():
    pyautogui.hotkey('win', '2')
    time.sleep(1)
    pyautogui.press('f11')

def open_terminal_tmux():
    open_run_box()
    # terminal path
    type_and_enter(r'"..."')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'shift', '6')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'alt', '1')
    type_and_enter("exit")
    type_and_enter("neofetch")


def open_terminal_vim():
    open_run_box()
    # terminal path
    type_and_enter(r'"..."')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'shift', '6')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'alt', '1')
    type_and_enter("exit")
    type_and_enter("nvim .")

def open_application():
    pyautogui.hotkey('alt', 'space')


# === Desktop 1: close all desktop that already created ===
close_extra_desktops()

# === Desktop 1: Open Brave in Fullscreen ===
open_run_box()
#brawser path
type_and_enter(r'"..."')
pyautogui.hotkey('alt', 'd')
type_and_enter("https://www.youtube.com/")
pyautogui.press('f11')

# === Desktop 2:linux termunal with linux ===
create_new_desktop()
switch_desktop_right()
open_terminal_vim()
pyautogui.press('f11')

# === Desktop 3: PowerShell ===
create_new_desktop()
switch_desktop_right()
open_terminal_tmux()
pyautogui.press('f11')

# === Desktop 4: VS Code ===
create_new_desktop()
switch_desktop_right()
# open_run_box()
# type_and_enter("code")
# pyautogui.press('f11')

# === move desktop 1 ===
switch_desktop_1()
print("Automation complete.")

