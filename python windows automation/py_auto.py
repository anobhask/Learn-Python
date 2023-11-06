import pyautogui
from time import sleep
import logging

x=10
y=12
## Logging configuration
logging.basicConfig(format='%(asctime)s %(message)s')

def load_animation(loading_time=1):
    anim_symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    i = 0
    load_count_for_second = len()
    for anim_count in range(64 * loading_time):
        i = (i + 1) % len(symbols)
        print('\r\033[K%s loading...' % anim_symbols[i], flush=True, end='')
        sleep(0.1)

def main():
    while True:
        # Get the current poistion
        mouse_cord = pyautogui.position()
        # Move the mouse cursor to the desired position
        pyautogui.moveTo(x, y)
        # Perform a right-click
        pyautogui.click(button="left")
        logging.warning(f"Mouse left Pos x:{x} y:{y}")
        pyautogui.moveTo(mouse_cord)
        logging.warning(f"Mouse left Pos x:{mouse_cord.x} y:{mouse_cord.y}")
        sleep(200)

try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    my_choice = input('Do you want to exit (Y/N):')
    if my_choice in ('y', 'Y'):
        print("exiting ......")
        exit()
    main()
finally:
    print("exited from loop")
    
