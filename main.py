import tkinter
import customtkinter as ctk
from PIL import Image, ImageTk
import qrcode
from tkinter import filedialog



root = ctk.CTk()
root.title("QRCode Generator")
root.after(0, root.configure(state = "zoomed"))
root.iconbitmap("assets/icon.ico")
currentImage = ""

def generate_qr_code(data = ""):
    global currentImage, firstFrame
    data = data_input.get(1.0, ctk.END)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    data_input.delete(1.0, ctk.END)
    firstFrame.forget()

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Files", "*.png")]
    )
    if file_path:
        with open(file_path, "wb")as file:
            img.save(file)
                
    currentImage = ""

    firstFrame.place(relx = 0, rely = 0, relwidth = 1,relheight = 1)


textImage = ImageTk.PhotoImage(Image.open("assets/file.png").resize((90, 90)))
imageImage = ImageTk.PhotoImage(Image.open("assets/picture.png").resize((90, 90)))


firstFrame = ctk.CTkFrame(root)
firstFrame.place(relx = 0, rely = 0, relwidth = 1,relheight = 1)

data_input = ctk.CTkTextbox(firstFrame, fg_color = "#333333", corner_radius=12, font = ("Calibri Light", 25, "bold"))
data_input.place(relx = 0.1, rely = 0.1, relwidth = 0.8,relheight = 0.3)
data_input.insert(1.0, "Enter your data here.")

button  = ctk.CTkButton(firstFrame, font = ("Calibri Light", 20), fg_color = "#0ad", hover_color="#00a1d1", cursor = "hand2", text = "Generate qrcode", command = generate_qr_code)
button.place(relx = 0.4, rely = 0.45, relwidth = 0.2,relheight = 0.07)



root.mainloop()