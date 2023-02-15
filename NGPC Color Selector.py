import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("NGPC Color Selector")

# Set the default values for R, G, and B
r_val = tk.IntVar(value=0)
g_val = tk.IntVar(value=0)
b_val = tk.IntVar(value=0)

# Create the input fields for R, G, and B
r_label = tk.Label(root, text="Red (0-15)")
r_label.grid(row=0, column=0, padx=10, pady=10)
r_spinbox = tk.Spinbox(root, from_=0, to=15, textvariable=r_val, width=5)
r_spinbox.grid(row=1, column=0, padx=10, pady=10)
g_label = tk.Label(root, text="Green (0-15)")
g_label.grid(row=0, column=1, padx=10, pady=10)
g_spinbox = tk.Spinbox(root, from_=0, to=15, textvariable=g_val, width=5)
g_spinbox.grid(row=1, column=1, padx=10, pady=10)
b_label = tk.Label(root, text="Blue (0-15)")
b_label.grid(row=0, column=2, padx=10, pady=10)
b_spinbox = tk.Spinbox(root, from_=0, to=15, textvariable=b_val, width=5)
b_spinbox.grid(row=1, column=2, padx=10, pady=10)

# Create a canvas to display the color square
canvas = tk.Canvas(root, width=100, height=100, bg="#000000", highlightthickness=1, highlightbackground="black")
canvas.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Create a text box to display the hex code of the color
hex_val = tk.StringVar(value="#000000")
output_text = tk.Text(root, height=1, font=("Courier", 14), bg="white", padx=5, pady=5, highlightthickness=0)
output_text.insert(tk.END, hex_val.get())
output_text.config(state="disabled")
output_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Create a text box to display the RGB values as unconverted values between 0 and 15
rgb_val = tk.StringVar(value="RGB(0,0,0)")
rgb_text = tk.Text(root, height=1, font=("Courier", 14), bg="white", padx=5, pady=5, highlightthickness=0)
rgb_text.insert(tk.END, rgb_val.get())
rgb_text.config(state="disabled")
rgb_text.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Create a function to update the color of the square and the output text box whenever any of the input fields are changed
def update_color(*args):
    r = max(0, min(r_val.get(), 15)) * 16
    g = max(0, min(g_val.get(), 15)) * 16
    b = max(0, min(b_val.get(), 15)) * 16
    color = f"#{r:02x}{g:02x}{b:02x}"
    canvas.config(bg=color)
    hex_val.set(color)
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, color)
    output_text.config(state="disabled")
    
    color2 = "RGB("+str(min(r_val.get(), 15))+","+str(min(g_val.get(), 15))+","+str(min(b_val.get(), 15))+")"
    rgb_text.config(state="normal")
    rgb_text.delete("1.0", tk.END)
    rgb_text.insert(tk.END, color2)
    rgb_text.config(state="disabled")

# Bind the update_color function to the changes of the input fields
r_val.trace_add("write", update_color)
g_val.trace_add("write", update_color)
b_val.trace_add("write", update_color)

# Start the main loop
root.mainloop()
