import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from rembg import remove
import os

class RemoveBG:
    def __init__(self, root):
        self.root = root
        self.root.title("Background Remover")
        self.root.geometry("900x500")
        self.root.configure(bg="#f4f4f4")
        
        self.input_path = None
        self.original_img = None
        self.result_img = None
        
        #frame kiri (untuk gambar original)
        self.left_frame = tk.Frame(self.root, bg="#f4f4f4", bd=2, relief="ridge")
        self.left_frame.place(x=20, y=20, width=400, height=400)
        
        #frame kanan (untuk gambar result)
        self.right_frame = tk.Frame(self.root, bg="#f4f4f4", bd=2, relief="ridge")
        self.right_frame.place(x=480, y=20, width=400, height=400)
        
        #tombol upload
        self.btn_open = tk.Button(self.root, text="Pilih gambar", command=self.open_image, 
                                    bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        self.btn_open.place(x=250, y=440, width=150)
        
        self.btn_remove = tk.Button(self.root, text="Hapus Backround", command=self.remove_background,
                                    bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
        self.btn_remove.place(x=500, y=440, width=200)
        
    def open_image(self):
        self.input_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
        )
        
        if self.input_path:
            img = Image.open(self.input_path)
            img.thumbnail((300, 380))
            self.original_img = ImageTk.PhotoImage(img)
            
            label = tk.Label(self.left_frame, image=self.original_img)
            label.image = self.original_img
            label.pack()
            
    def remove_background(self): 
        if not self.input_path:
            return
        
        input_image = Image.open(self.input_path)
        output_image = remove(input_image)
        
        #simpan gambar hasil
        output_path = os.path.splitext(self.input_path)[0] + "_no_bg.png"
        output_image.save(output_path)
        
        output_image.thumbnail((300, 380))
        self.result_img = ImageTk.PhotoImage(output_image)
        
        label = tk.Label(self.right_frame, image=self.result_img)
        label.image = self.result_img
        label.pack()
        
        print("Disimpan di:", output_path)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = RemoveBG(root)
    root.mainloop()
            