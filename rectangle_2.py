from figure import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
sq_1 = Square(5)
sq_2 = Square(10)
cir_1 = Circle(5)
cir_2 = Circle(10)

figures = [rect_1, rect_2, sq_1, sq_2, cir_1, cir_2]

for fig in figures:
    # print(fig.get_area())
    if isinstance(fig, Square):
        print(fig.get_area_square())
    elif isinstance(fig, Circle):
        print(fig.get_area_circle())
    else:
        print(fig.get_area())