#Requires AutoHotkey v2.0

Persistent()

; Load the DLL that enables virtual desktop switching
DllCall("LoadLibrary", "Str", "VirtualDesktopAccessor.dll", "Ptr")

; --- Functions ---

switchDesktop(index) {
    DllCall("VirtualDesktopAccessor.dll\GoToDesktopNumber", "Int", index)
    hideTaskbar()
    Sleep(300)  ; Give time for desktop switch to complete
    focusCurrentWindow()
   
}

hideTaskbar() {
    taskbar := WinExist("ahk_class Shell_TrayWnd")
    start := WinExist("ahk_class Button")
    if taskbar
        WinHide("ahk_id " taskbar)
    if start
        WinHide("ahk_id " start)
}



focusCurrentWindow() {
    ; Simulate Alt+Tab then Shift+Tab to trigger native window focus
    Send("{Alt down}")
    Sleep(50)
    Send("{Tab}")
    Sleep(100)
    Send("{Shift down}{Tab}")
    Sleep(50)
    Send("{Shift up}{Alt up}")
}

; --- Hotkeys ---

!1::switchDesktop(0)
!2::switchDesktop(1)
!3::switchDesktop(2)
!4::switchDesktop(3)



; Vim-style navigation
!h::Send("{Left}")
!j::Send("{Down}")
!k::Send("{Up}")
!l::Send("{Right}")
