import subprocess, os

def create_canvas(width, height):
    canvas = [[' ' for _ in range(width)] for _ in range(height)]
    return canvas

def draw_rect(x, y, w, h, canvas):
    rect_char = 'O'

    for i in range(y, y+h):
        for j in range(x, x+w):
            canvas[i][j] = rect_char

def push_to_console(canvas):
    for row in canvas:
        print(''.join(row))

def clear_screen():
    if os.name == 'nt':
        subprocess.run("cls", shell=True)
    elif os.name == 'posix':
        subprocess.run("clear", shell=True)