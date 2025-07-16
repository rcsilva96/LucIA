from tkinter import Tk, Label
from PIL import Image, ImageTk

avatar_path = "assets/image/lucia.jpg"

class AvatarWindow:
    def __init__(self, image_path):
        self.root = Tk()
        self.root.title("LucIA")
        self.root.resizable(False, False)
        try:
            img = Image.open(image_path).resize((300, 300), Image.LANCZOS)
            self.avatar_img = ImageTk.PhotoImage(img)
            self.label = Label(self.root, image=self.avatar_img)
            self.label.pack()
            self.status_label = Label(self.root, text="Pronta para ajudar!", font=('Arial', 12))
            self.status_label.pack(pady=10)
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")
            self.root.destroy()
            raise

    def update_status(self, text):
        self.status_label.config(text=text)

    def run(self):
        self.root.mainloop()

def iniciar_interface():
    window = AvatarWindow(avatar_path)
    window.run()
