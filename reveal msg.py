from tkinter import Tk, Button, filedialog, messagebox
from PIL import Image

def retrieve_message():
    image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if not image_path:
        return

    image = Image.open(image_path)
    image = image.convert("RGB")
    data = list(image.getdata())

    binary_message = ""
    for pixel in data:
        binary_message += str(pixel[0] & 0x1)

    message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    message = message.split('\x00', 1)[0]

    messagebox.showinfo("Hidden Message", message)

app = Tk()
app.title("Picture - Retrieve Message")

retrieve_button = Button(app, text="Retrieve Message", command=retrieve_message)
retrieve_button.pack()

app.mainloop()
