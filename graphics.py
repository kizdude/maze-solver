from tkinter import Tk, BOTH, Canvas



class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Line():
    def __init__(self, point_1 : Point, point_2 : Point):
        self.x1 = point_1.x
        self.y1 = point_1.y
        self.x2 = point_2.x
        self.y2 = point_2.y

    def draw(self, canvas : Canvas, fill_colour : str):
        canvas.create_line(
            self.x1, self.y1, self.x2, self.y2, fill=fill_colour, width=2
        )



class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
            
    def close(self):
        self.__running = False

    def draw_line(self, line : Line, fill_colour : str):
        line.draw(self.__canvas, fill_colour)

