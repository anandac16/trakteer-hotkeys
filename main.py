import ctypes
from ctypes import wintypes
import time

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# msdn.microsoft.com/en-us/library/dd375731
VK_TAB  = 0x09
VK_MENU = 0x12
VK_CONTROL = 0x11
VK_SHIFT = 0x10
VK_1 = 0x31
VK_2 = 0x32
VK_3 = 0x33
VK_4 = 0x34
VK_5 = 0x35
VK_A = 0x41
VK_B = 0x42
VK_C = 0x43
VK_D = 0x44
VK_E = 0x45
VK_F = 0x46
VK_G = 0x47
VK_H = 0x48
VK_I = 0x49
VK_J = 0x4A
VK_K = 0x4B
VK_L = 0x4C
VK_M = 0x4D
VK_N = 0x4E
VK_O = 0x4F
VK_P = 0x50
VK_Q = 0x51
VK_R = 0x52
VK_S = 0x53
VK_T = 0x54
VK_U = 0x55
VK_V = 0x56
VK_W = 0x57
VK_X = 0x58
VK_Y = 0x59
VK_Z = 0x5A
VK_LWIN = 0x5B
VK_F4 = 0x73
VK_SPACE = 0x20
VK_LCONTROL = 0xA2
# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def AltTab():
    """Press Alt+Tab and hold Alt key for 2 seconds
    in order to see the overlay.
    """
    PressKey(VK_MENU)   # Alt
    PressKey(VK_TAB)    # Tab
    ReleaseKey(VK_TAB)  # Tab~
    # time.sleep(2)
    ReleaseKey(VK_MENU) # Alt~

def AltF4():
    for i in range(0, 2):   # force ALT+F4 buat yg ada exit confirmation kayak valo xd
        PressKey(VK_MENU)
        PressKey(VK_F4)
        time.sleep(0.2)
        ReleaseKey(VK_MENU)
        ReleaseKey(VK_F4)

def throwGun():
    PressKey(VK_G)
    ReleaseKey(VK_G)

def throwGun5Sec():
    print("Pressing G for 5 seconds...")
    for i in range(0,5):
        PressKey(VK_G)
        ReleaseKey(VK_G)
        time.sleep(1)

def knifeOnly():
    PressKey(VK_3)
    ReleaseKey(VK_3)

def knifeOnly5Sec():
    print("Pressing 3 for 5 seconds...")
    for i in range(0,5):
        PressKey(VK_3)
        ReleaseKey(VK_3)
        time.sleep(1)

def useUltimate():
    PressKey(VK_X)
    ReleaseKey(VK_X)
    PressKey(VK_Z)
    ReleaseKey(VK_Z)

def jumpingJack():
    print("Pressing Space for 5 seconds...")
    for i in range(0,5):
        PressKey(VK_SPACE)
        ReleaseKey(VK_SPACE)
        time.sleep(1)

def teaBag():
    print("Pressing ctrl for 5 seconds")
    for i in range(0,5):
        PressKey(VK_LCONTROL)
        time.sleep(0.2)
        ReleaseKey(VK_LCONTROL)
        time.sleep(0.5)

def crouchOnly():
    print("Pressing ctrl for 5 seconds")
    for i in range(0,5):
        PressKey(VK_LCONTROL)
        time.sleep(1)
    ReleaseKey(VK_LCONTROL)

def moonWalk():
    print("Pressing S for 5 seconds")
    for i in range(0,10):
        ReleaseKey(VK_W)
        ReleaseKey(VK_A)
        ReleaseKey(VK_D)
        PressKey(VK_S)
        time.sleep(0.5)
    ReleaseKey(VK_S)

def runCmd(cmd):
    cmd = cmd.lower()
    if cmd == "!AltTab".lower():
        return AltTab()
    elif cmd == "!throwGun".lower():
        return throwGun()
    elif cmd == "!throwGun5Sec".lower():
        return throwGun5Sec()
    elif cmd == "!knifeOnly".lower():
        return knifeOnly()
    elif cmd == "!knifeOnly5Sec".lower():
        return knifeOnly5Sec()
    elif cmd == "Selalu Berkarya!".lower(): # for testing
        return AltTab()
    elif cmd == "!jumpingJack".lower():
        return jumpingJack()
    elif cmd == "!crouchOnly".lower():
        return crouchOnly()
    elif cmd == "!teaBag".lower():
        return teaBag()
    elif cmd == "!moonWalk".lower():
        return moonWalk()

