# Importing the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Lab 3 Assignment"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Lab 3 Assignment")

# Set background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the sun
arcade.draw_circle_filled(200, 580, 22, arcade.color.YELLOW)

# Draw the sand
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BISQUE,)

# rectangle for ocean
arcade.draw_lrtb_rectangle_filled(0, 800, 230, 200, arcade.color.BLUE)

# --- Draw the beach ---

# Beach ball
arcade.draw_circle_filled(300, 200, 50, arcade.color.ICTERINE)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it
arcade.run()
