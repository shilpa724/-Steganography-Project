from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from PIL import Image

def hide_message():
    image_path = filedialog.askopenfilename()
    image = Image.open(image_path)
    image = image.convert("RGB")
    data = list(image.getdata())

    message = message_entry.get()
    if not message:
        messagebox.showerror("Error", "Message cannot be empty")
        return

    binary_message = ''.join(format(ord(c), '08b') for c in message) + '00000000'

    if len(binary_message) > len(data):
        messagebox.showerror("Error", "Message is too long for the selected image")
        return

    for i in range(len(binary_message)):
        pixel = list(data[i])
        pixel[0] = pixel[0] & 0xFE | int(binary_message[i])
        data[i] = tuple(pixel)

    image.putdata(data)
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    image.save(save_path)
    messagebox.showinfo("Success", "Message hidden in image")

app = Tk()
app.title("Steganography - Hide Message")

message_label = Label(app, text="Enter Message:")
message_label.pack()

message_entry = Entry(app, width=50)
message_entry.pack()

hide_button = Button(app, text="Hide Message", command=hide_message)
hide_button.pack()

app.mainloop()
