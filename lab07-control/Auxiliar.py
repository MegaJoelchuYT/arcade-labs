        arcade.draw_rectangle_filled(200, 200, 200, 75, arcade.color.RED)
        arcade.draw_rectangle_filled(200, 250, 125, 55, arcade.color.RED)
        arcade.draw_circle_filled(250, 150, 25, arcade.color.ASH_GREY)
        arcade.draw_circle_filled(150, 150, 25, arcade.color.ASH_GREY)

        self.carTire = CarTires(50, 50, 0, 0, 15)
        self.carChassis = CarChassis(100, 150, 0, 0, 55)