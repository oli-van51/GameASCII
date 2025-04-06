import subprocess, os
from pynput import keyboard

def create_canvas(width, height):
    canvas = [[' ' for _ in range(width)] for _ in range(height)]
    return canvas

def draw_rect(x, y, w, h, canvas):
    rect_char = 'O'

    for i in range(y, y+h):
        for j in range(x, x+w):
            try:
                canvas[i][j] = rect_char
            except IndexError:
                pass

def push_to_console(canvas):
    for row in canvas:
        print(''.join(row))

def clear_screen(canvas):
    if os.name == 'nt':
        subprocess.run("cls", shell=True)
    elif os.name == 'posix':
        subprocess.run("clear", shell=True)

    for row in canvas:
        for i in range(len(row)):
            row[i] = ' '
    
    

key_states = {"a": False, "d": False, "w": False, "s": False}

def on_press(key):
    try:
        if key.char in key_states:
            key_states[key.char] = True
    except AttributeError:
        pass

def on_release(key):
    try:
        if key.char in key_states:
            key_states[key.char] = False
    except AttributeError:
        pass
    if key == keyboard.Key.esc:
        return False
    
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()


def get_axis(axis: str = "horizontal", value: int = 1):
    if not listener.running:
        return None
    if axis == "horizontal":
        if key_states["a"]:
            return -value
        elif key_states["d"]:
            return value
        else:
            return 0
    elif axis == "vertical":
        if key_states["w"]:
            return -value
        elif key_states["s"]:
            return value
        else:
            return 0