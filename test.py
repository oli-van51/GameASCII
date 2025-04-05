import gameASCII as ga

canvas = ga.create_canvas(8, 4)

ga.clear_screen()

ga.draw_rect(1,0,2,2,canvas)

ga.draw_rect(3,0,2,3,canvas)

ga.push_to_console(canvas)