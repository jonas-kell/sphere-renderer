import tkinter

from coordinates import (
    get_2d_coordinates_of_pentagons,
)

from translate_coordinates import get_2d_coordinate_from_circle_coordinate

from PIL import ImageGrab

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

# get the image info of the input_canvas
def get_in_image():
    x = root.winfo_rootx() + input_canvas.winfo_x()
    y = root.winfo_rooty() + input_canvas.winfo_y()
    x1 = x + input_canvas.winfo_width()
    y1 = y + input_canvas.winfo_height()
    return ImageGrab.grab().crop((x, y, x1, y1))


# draw on the output_canvas
def draw_globe_projection():
    in_image = get_in_image()

    print("started drawing sphere")
    output_canvas.delete("all")
    output_canvas.create_rectangle(0, 0, in_width, in_height, fill="white")

    # 80, 3 gives good resolution, but takes ca. 30 sek
    radius = 30
    pixel_width = 5
    radius_squared = radius * radius

    for i in range(-radius, radius + 1):
        i_sqared = i * i
        for j in range(-radius, radius + 1):
            j_squared = j * j
            if i_sqared + j_squared <= radius_squared:

                # get coordinate to look up color from
                x_2d, y_2d = get_2d_coordinate_from_circle_coordinate(
                    i / radius, j / radius
                )

                # look up color
                x_canvas, y_canvas = coords_to_2d_canvas_coords(x_2d, y_2d)
                color = "#%02x%02x%02x" % in_image.getpixel((x_canvas, y_canvas))

                # render to canvas
                output_canvas.create_rectangle(
                    out_width // 2 + pixel_width * i,
                    out_height // 2 - pixel_width * j,
                    out_width // 2 + pixel_width * i + 2 * pixel_width - 2,
                    out_height // 2 - pixel_width * j + 2 * pixel_width - 2,
                    fill=color,
                    width=0,
                )

    print("finished drawing sphere")


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


def button_event(e):
    print("update trigger")
    draw_globe_projection()


# Bind the mouse_move function
input_canvas.bind("<B1-Motion>", mouse_move)
root.bind("<Return>", button_event)

root.mainloop()
