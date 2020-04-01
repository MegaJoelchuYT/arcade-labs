""" Sprite Sample Program """

import random
import arcade
import math

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.25
SPRITE_SCALING_BALL = 0.05
SPRITE_SCALING_GRAY = 0.75
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Gray(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):

        """ Update the ball's position. """
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed


class Ball(arcade.Sprite):

    def update(self):
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            # Reset the coin to a random spot above the screen
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.ball_list = None
        self.gray_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLUE)
        self.coin_sound = arcade.load_sound("mario-coin.mp3")
        self.fail_sound = arcade.load_sound("correct-cbt-sound.mp3")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.gray_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            ball = Ball("okegreatultramaster-ball-super-mario-world-boo-sprite-11562983716xog8m5pbnj.png", SPRITE_SCALING_BALL)

            # Position the coin
            ball.center_x = random.randrange(SCREEN_WIDTH)
            ball.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.ball_list.append(ball)

        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            gray = Gray("3696.png", SPRITE_SCALING_GRAY)

            # Position the coin
            gray.center_x = random.randrange(SCREEN_WIDTH)
            gray.center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            gray.circle_radius = random.randrange(150, 800)

            # Random start angle from 0 to 2pi
            gray.circle_angle = random.random() * 30 * math.pi

            # Add the coin to the lists
            self.gray_list.append(gray)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.ball_list.draw()
        self.gray_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.ball_list.update()

        # Generate a list of all sprites that collided with the player.
        ball_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.ball_list)
        # Loop through each colliding sprite, remove it, and add to the score.
        for ball in ball_hit_list:
            ball.remove_from_sprite_lists()
            self.score += 1
            arcade.sound.play_sound(self.coin_sound)

        self.gray_list.update()

        # Generate a list of all sprites that collided with the player.
        gray_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.gray_list)
        # Loop through each colliding sprite, remove it, and add to the score.
        for gray in gray_hit_list:
            gray.remove_from_sprite_lists()
            self.score -= 1
            arcade.sound.play_sound(self.fail_sound)
            
        if self.ball_list == None:
            output = f"GAME OVER"
            arcade.draw_text(output, 250, 300, arcade.color.WHITE, 30)
def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()