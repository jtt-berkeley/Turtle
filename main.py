from shapes import Triangle, Rectangle, Oval
# creates an instance of Rectangle object
rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("orange")

rect2 = Rectangle()
rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")
rect2.set_x(-10)
rect2.set_y(10)

rect1.draw()
rect2.draw()