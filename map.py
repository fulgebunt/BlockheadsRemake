import tkinter as tk

class Map:
    def __init__(self, root, show_grid):
        self.canvas = tk.Canvas(root, width=300, height=600, bg="white")
        self.canvas.pack()

        self.offset_x = 0
        self.offset_y = 0
        self.dragging = False
        self.show_grid = show_grid

        self.rows = 100  # number of rows in the grid
        self.columns = 50  # number of columns in the grid
        self.tiles = [['' for _ in range(self.columns)] for _ in range(self.rows)]

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_canvas_release)

        self.draw_grid()

    def on_canvas_click(self, event):
        grid_x = (event.x - self.offset_x) // 30
        grid_y = (event.y - self.offset_y) // 30

        tile_color = self.tiles[grid_y][grid_x] if 0 <= grid_x < self.columns and 0 <= grid_y < self.rows else 'None'
        print(f"Clicked on grid coordinate: ({grid_x}, {grid_y}), Tile Color: {tile_color}")

        self.drag_start_x = event.x
        self.drag_start_y = event.y
        self.dragging = True

    def on_canvas_drag(self, event):
        if self.dragging:
            delta_x = event.x - self.drag_start_x
            delta_y = event.y - self.drag_start_y
            self.offset_x += delta_x
            self.offset_y += delta_y
            self.drag_start_x = event.x
            self.drag_start_y = event.y
            self.draw_grid()

    def on_canvas_release(self, event):
        self.dragging = False

    def draw_grid(self):
        self.canvas.delete("all")

        start_col = max(0, -self.offset_x // 30 - 2)
        end_col = min(self.columns, start_col + 13)
        start_row = max(0, -self.offset_y // 30 - 2)
        end_row = min(self.rows, start_row + 23)

        if self.show_grid:
            for i in range(start_col, end_col + 1):
                self.canvas.create_line(i * 30 + self.offset_x, 0, i * 30 + self.offset_x, 600, fill="black")
            for i in range(start_row, end_row + 1):
                self.canvas.create_line(0, i * 30 + self.offset_y, 300, i * 30 + self.offset_y, fill="black")

        for x in range(start_col, end_col):
            for y in range(start_row, end_row):
                tile_color = self.tiles[y][x]
                if tile_color:  # Only draw non-empty tiles
                    self.canvas.create_rectangle(
                        x * 30 + self.offset_x, y * 30 + self.offset_y,
                        (x + 1) * 30 + self.offset_x, (y + 1) * 30 + self.offset_y,
                        fill=tile_color, outline=""
                    )

    def set_tile(self, x, y, tile_color):
        """Sets the color of the tile at grid coordinates (x, y) to tile_color."""
        if 0 <= x < self.columns and 0 <= y < self.rows:
            self.tiles[y][x] = tile_color

    def redraw(self):
        self.draw_grid()