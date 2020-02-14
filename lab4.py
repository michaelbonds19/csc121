import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_sun():
    """ Draw the sun """
    arcade.draw_circle_filled(200, 580, 22, arcade.color.YELLOW)

def draw_sand():
    """ Draw the sand """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 5, 0, arcade.color.BISQUE)

def draw_ocean():
    """ Draw rectangle for ocean"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 200, arcade.color.BLUE)

def draw_beach(x, y):
    """ Draw the beach """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.BLUE, 5)

    # Beach ball
    arcade.draw_circle_filled(x - 300, 200 - y, 50, arcade.color.ICTERINE)

def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()
    
    draw_sun()
    draw_sand()
    draw_ocean()
    draw_beach(on_draw.beach1_x, 140)
    draw_beach(450, 180)



    on_draw.beach1_x += 1



on_draw.beach1_x = 150

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing With Functions")
    arcade.set_background_color(arcade.color.BLUE)
    
    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()