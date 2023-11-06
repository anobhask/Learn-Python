
import pyautogui, time, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        CurserPos = pyautogui.position()
        print(type(CurserPos))
        sys.stdout.flush()
except KeyboardInterrupt:
    print("Pressed Ctrl+C exiting----")
    exit()