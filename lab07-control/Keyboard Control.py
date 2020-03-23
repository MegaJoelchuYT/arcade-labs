import arcade
from arcade import Sound

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 5
DEAD_ZONE = 0.02


class Car:
    def __init__(self, position_x, position_y, change_x, change_y, radius):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, arcade.color.ASH_GREY)
        arcade.draw_circle_filled(self.position_x + 100, self.position_y, self.radius, arcade.color.ASH_GREY)
        arcade.draw_rectangle_filled(self.position_x + 50, self.position_y + 50, self.radius + 145, self.radius + 60, arcade.color.RED)
        arcade.draw_rectangle_filled(self.position_x + 50, self.position_y + 100, self.radius + 70, self.radius + 40, arcade.color.RED)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            
            self.position_x = self.radius


        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

class Human:
    def __init__(self, position_x, position_y, radius):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x + 50, self.position_y + 100, self.radius, arcade.color.BLACK)
        arcade.draw_rectangle_filled(self.position_x + 50, self.position_y + 75, self.radius, self.radius + 40, arcade.color.BLACK)
        arcade.draw_rectangle_filled(self.position_x + 50, self.position_y + 75, self.radius + 40, self.radius - 5, arcade.color.BLACK)
        arcade.draw_rectangle_filled(self.position_x + 58, self.position_y + 35, self.radius - 5, self.radius + 20, arcade.color.BLACK, 30)
        arcade.draw_rectangle_filled(self.position_x + 40, self.position_y + 35, self.radius - 5, self.radius + 20, arcade.color.BLACK, -30)

class ForbiddenSign:
    def __init__(self, position_x, position_y, change_x, change_y, radius):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, arcade.color.RED)
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.radius, self.radius - 30, arcade.color.WHITE)
        arcade.draw_rectangle_filled(self.position_x, self.position_y - 85, self.radius - 30, self.radius + 50, arcade.color.ASH_GREY)
        arcade.draw_rectangle_filled(self.position_x + 60, self.position_y + 35, self.radius - 20, self.radius + 30, arcade.color.DARK_GREEN)
        arcade.draw_rectangle_filled(self.position_x + 60, self.position_y + 85, self.radius, self.radius + 20, arcade.color.DARK_GREEN)
        arcade.draw_circle_filled(self.position_x + 60, self.position_y + 100, self.radius - 35, arcade.color.RED)
        arcade.draw_circle_filled(self.position_x + 60, self.position_y + 85, self.radius - 35, arcade.color.AMBER)
        arcade.draw_circle_filled(self.position_x + 60, self.position_y + 70, self.radius - 35, arcade.color.GREEN)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)
        self.laser_sound = arcade.load_sound("laser.ogg")
        self.claxon_sound = arcade.load_sound("vehicle039.mp3")
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.car = Car(50, 50, 0, 0, 15)
        self.human = Human(50, 50, 15)
        self.forbiddensign = ForbiddenSign(500, 150, 0, 0, 40)

        # Get a list of all the game controllers that are plugged in
        joysticks = arcade.get_joysticks()

        # If we have a game controller plugged in, grab it and
        # make an instance variable out of it.
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no joysticks.")
            self.joystick = None


    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(300, 400, 300, 200, arcade.color.WOOD_BROWN)
        arcade.draw_arc_filled(350, 300, 100, 100, arcade.color.FERRARI_RED, 0, 180, 0, 150)
        arcade.draw_lrtb_rectangle_filled(340, 360, 250, 200, arcade.color.DARK_BROWN)
        arcade.draw_lrtb_rectangle_filled(0, 1000, 199, 150, arcade.color.APPLE_GREEN)
        arcade.draw_lrtb_rectangle_filled(0, 1000, 149, 50, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(0, 1000, 49, 0, arcade.color.APPLE_GREEN)
        arcade.draw_lrtb_rectangle_filled(25, 50, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(75, 100, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(125, 150, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(175, 200, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(225, 250, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(275, 300, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(325, 350, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(375, 400, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(425, 450, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(475, 500, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(525, 550, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(575, 600, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(625, 650, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(675, 700, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(725, 750, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(775, 800, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(825, 850, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(875, 900, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(925, 950, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_lrtb_rectangle_filled(975, 1000, 101, 100, arcade.color.ANTIQUE_WHITE)
        arcade.draw_triangle_filled(400, 200, 600, 600, 800, 200, arcade.color.DARK_BROWN)
        arcade.draw_triangle_filled(500, 400, 600, 600, 700, 400, arcade.color.ANTIQUE_WHITE)
        arcade.draw_circle_filled(15, 600, 75, arcade.color.GOLDEN_YELLOW, 50)
        self.car.draw()
        self.human.draw()
        self.forbiddensign.draw()

    def update(self, delta_time):
        self.car.update()

        # Update the position according to the game controller
        if self.joystick:

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.x) < DEAD_ZONE:
                self.forbiddensign.change_x = 0
            else:
                self.forbiddensign.change_x = self.joystick.x * MOVEMENT_SPEED

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.y) < DEAD_ZONE:
                self.forbiddensign.change_y = 0
            else:
                self.forbiddensign.change_y = -self.joystick.y * MOVEMENT_SPEED

            self.forbiddensign.update()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.human.position_x = x
        self.human.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
            arcade.sound.play_sound(self.laser_sound)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)
            arcade.sound.play_sound(self.claxon_sound)

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.car.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.car.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.car.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.car.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.car.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.car.change_y = 0


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()