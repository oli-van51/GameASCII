import gameASCII as ga
import time

canvas = ga.create_canvas(100, 50)

ga.clear_screen(canvas)

x = 10
y = 10

FPS = 1

run = True
while run:

    ga.clear_screen(canvas)

    start_time = time.time()

    x_dir = ga.get_axis("horizontal", 1)

    y_dir = ga.get_axis("vertical", 1)

    if x_dir is None or y_dir is None:
        run = False
        break

    x += x_dir
    y += y_dir

    ga.draw_rect(x,y,2,2,canvas)

    ga.draw_rect(3,0,2,3,canvas)

    ga.push_to_console(canvas)

    elapsed = time.time() - start_time
    t_sleep = max(0, (1/FPS) - elapsed)
    time.sleep(t_sleep)