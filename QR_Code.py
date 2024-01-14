import qrcode
import tkinter as tk
from tkinter import messagebox

def QR_MAKER_DOWNLOAD():
    try:

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        a='.png'
        link = url_entry.get()
        name= name_entry.get()
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save(name+a)
        messagebox.showinfo("Success", "QR code generated")
        return img
    except Exception as e:
        messagebox.showerror("Error", str(e))




root = tk.Tk()
root.title("QR maker")




url_label = tk.Label(root, text="Enter File URL or Link: ")
url_label.pack()

url_entry = tk.Entry(root, width=40)
url_entry.pack()

url_label1= tk.Label(root, text="Enter name: ")
url_label1.pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()


download_button = tk.Button(root, text="convert", command=QR_MAKER_DOWNLOAD)
download_button.pack()




root.mainloop()




