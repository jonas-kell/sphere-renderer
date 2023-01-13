import tkinter
from coordinates import (
    get_2d_coordinates_of_pentagons,
    get_3d_coordinates_of_pentagons,
    get_2d_coordinates,
    get_3d_coordinates,
    get_2d_to_3d,
    get_3d_to_2d,
)

root = tkinter.Tk()
output_canvas = tkinter.Canvas(root)
input_canvas = tkinter.Canvas(root)

# configure canvases
input_canvas.configure(width=500, height=500)
output_canvas.configure(width=500, height=500)
output_canvas.pack(side="left")
input_canvas.pack(side="right")
root.update()  # needed so that width and height are correct

# init canvases
in_width = input_canvas.winfo_width()
in_height = input_canvas.winfo_height()
out_width = output_canvas.winfo_width()
out_height = output_canvas.winfo_height()

input_canvas.create_rectangle(0, 0, in_width, in_height, fill="blue")

pentagon_side_length_2d = 50

pentagons = get_2d_coordinates_of_pentagons()


def coords_to_2d_canvas_coords(x, y):
    return (
        x * pentagon_side_length_2d + in_width // 2,
        -y * pentagon_side_length_2d + in_height // 2,
    )


for pentagon in pentagons:
    for i in range(0, 5):
        point_a_x, point_a_y = coords_to_2d_canvas_coords(
            pentagon[i][0], pentagon[i][1]
        )
        point_b_x, point_b_y = coords_to_2d_canvas_coords(
            pentagon[(i + 1) % 5][0], pentagon[(i + 1) % 5][1]
        )

        input_canvas.create_line(point_a_x, point_a_y, point_b_x, point_b_y, width=2)


def mouse_move(e):
    size = 20
    x = e.x
    y = e.y
    input_canvas.create_oval(
        x - size // 2,
        y - size // 2,
        x + size // 2,
        y + size // 2,
        fill="green",
        width=0,
    )


# Bind the mouse_move function
input_canvas.bind("<B1-Motion>", mouse_move)

root.mainloop()
