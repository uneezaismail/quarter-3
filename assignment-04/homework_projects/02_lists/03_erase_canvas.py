# # Implement an 'eraser' on a canvas.

# # The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import tkinter as tk

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserCanvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        
        # Create a grid of blue rectangles
        self.cells = []
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                rect = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")
                self.cells.append(rect)

        # Create the eraser
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")
        
        # Bind mouse motion to eraser movement
        self.canvas.bind("<Motion>", self.move_eraser)

    def move_eraser(self, event):
        """Moves the eraser with the mouse and erases overlapping cells."""
        self.canvas.coords(self.eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
        self.erase_objects(event.x, event.y)

    def erase_objects(self, x, y):
        """Changes the color of overlapping objects to white, simulating erasing."""
        overlapping = self.canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        for obj in overlapping:
            if obj != self.eraser:
                self.canvas.itemconfig(obj, fill="white")


root = tk.Tk()
root.title("Eraser Tool")
app = EraserCanvas(root)
root.mainloop()
