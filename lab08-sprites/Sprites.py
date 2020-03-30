""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.25
SPRITE_SCALING_BALL = 0.05
SPRITE_SCALING_GRAY = 0.5
COIN_COUNT = 100

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


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
            ball = arcade.Sprite("okegreatultramaster-ball-super-mario-world-boo-sprite-11562983716xog8m5pbnj.png", SPRITE_SCALING_BALL)

            # Position the coin
            ball.center_x = random.randrange(SCREEN_WIDTH)
            ball.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.ball_list.append(ball)

        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            gray = arcade.Sprite("3696.png", SPRITE_SCALING_GRAY)

            # Position the coin
            gray.center_x = random.randrange(SCREEN_WIDTH)
            gray.center_y = random.randrange(SCREEN_HEIGHT)

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

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()