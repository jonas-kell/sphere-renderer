import tkinter

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
