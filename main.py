import tkinter as tk
import map
import worldgen



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Draggable Grid")

    show_grid_input = input("Enter 0 to show grid lines, 1 to hide them: ")
    while show_grid_input not in ["0", "1"]:
        print("Invalid input. Please enter 0 or 1.")
        show_grid_input = input("Enter 0 to show grid lines, 1 to hide them: ")

    app = map.Map(root, show_grid_input == "0")
    array = worldgen.generateRandomMap()
    for i in range(100):
        for j in range(100):
            app.set_tile(i, j, array[i][j])

    app.redraw()
    #app.set_tile(3, 4, "#ff0000")  # Example usage of set_tile
    #app.set_tile(6, 8, "#00ff00")

    root.mainloop()
