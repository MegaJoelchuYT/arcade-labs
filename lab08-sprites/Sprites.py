import arcade
from arcade import Sound

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 5


class Sprite:
    def __init__(self, position_x, position_y):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.Sprite("130px-Joven_ROZA.png", 0.05, 50, 50, 30, 30, self.position_x, self.position_y, self.position_x, self.position_y)




class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.sprite = Sprite(50, 50)


    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.set_background_color(arcade.color.BLUE)
        arcade.start_render()
        self.sprite.draw()

    def update(self, delta_time):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.sprite.position_x = x
        self.sprite.position_y = y


def main():
    window = MyGame(640, 480, "Sprites")
    arcade.run()


main()