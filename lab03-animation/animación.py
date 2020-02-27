import arcade

arcade.open_window(800, 600, "Drawing Example")

def draw_house():
    arcade.draw_lrtb_rectangle_filled(300, 400, 300, 200, arcade.color.WOOD_BROWN)
    arcade.draw_arc_filled(350, 300, 100, 100, arcade.color.FERRARI_RED, 0, 180, 0, 150)
    arcade.draw_lrtb_rectangle_filled(340, 360, 250, 200, arcade.color.DARK_BROWN)

def draw_road():
    arcade.draw_lrtb_rectangle_filled(0, 1000, 149, 50, arcade.color.BLACK)
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

def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, 1000, 199, 150, arcade.color.APPLE_GREEN)
    arcade.draw_lrtb_rectangle_filled(0, 1000, 49, 0, arcade.color.APPLE_GREEN)

def draw_mountain():
    arcade.draw_triangle_filled(400, 200, 600, 600, 800, 200, arcade.color.DARK_BROWN)
    arcade.draw_triangle_filled(500, 400, 600, 600, 700, 400, arcade.color.ANTIQUE_WHITE)

def draw_sun(x,y):
    arcade.draw_point(x,y, arcade.color.AERO_BLUE, 5)
    arcade.draw_circle_filled(15 + x, 600 + y, 75, arcade.color.GOLDEN_YELLOW, 50)

def on_draw(delta_time):
    arcade.start_render()

    on_draw.sun_x = 25

    draw_house()
    draw_road()
    draw_grass()
    draw_mountain()
    draw_sun(on_draw.sun_x,0)
    draw_sun(0,0)

    on_draw.sun_x += 100


def main():
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()