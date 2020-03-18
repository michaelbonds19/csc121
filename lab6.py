import arcade

def draw_section_outlines():
    color = arcade.color.BLACK

    # Draw squares on the bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, color)
    arcade.draw_rectangle_outline(450, 150, 300, 300, color)
    arcade.draw_rectangle_outline(750, 150, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, color)

    # Draw squares on the bottom
    arcade.draw_rectangle_outline(150, 450, 300, 300, color)
    arcade.draw_rectangle_outline(450, 150, 300, 300, color)
    arcade.draw_rectangle_outline(750, 150, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, color)

def draw_section_1():
    y = -5
    for row in range(30):
        x = 5
        y += 10
        for column in range(30):
            x += 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def draw_section_2():
    y = -5
    count = 2
    for row in range(30):
       x = 295
       y += 10
       for column in range(30):
           x += 10
           if count % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
           else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
           count += 1

def draw_section_3():
    y = -5
    count = 2
    for row in range(30):
        x = 595
        y += 10
        count += 1
        for column in range(30):
            x += 10
            if count % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
   
def draw_section_4():
    y = -5
    count = 2
    for row in range(30):
        x = 895
        y += 10
        count += 1
        for column in range(30):
            x += 10
            if count % 2 == 0 and x < 1195 and y < 295:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            elif y >= 295 or x >= 1195:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
                count += 1

def draw_section_5():
    y = 295
    a = 0
    for row in range(30):
        x = 5 + a
        y += 10
        a += 10
        for column in range(30):
            if x < 300:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            x += 10

def draw_section_6():
    y = 295
    a = 305
    for row in range(30):
        x = 600 - a
        y += 10
        a += 10
        for column in range(30):
            if x < 600 and x > 300:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            x += 10    

def draw_section_7():
    y = 295 
    a = 315
    for row in range(30):
        y += 10
        x = 1205
        a += 1
        for column in range(30):
            if x < 900 and x > 600:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            x += 10

def draw_section_8():
    y = 295
    a = 0
    for row in range(30):
        y += 10
        x = 1205
        a += 1
        for column in range(30):
            x -= 10
            if x > 900  and x < 1200:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()

if __name__ == '__main__':
    main()
        