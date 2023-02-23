from tkinter import *
import tkinter.messagebox


class SpeedTestWpm:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Test")
        self.root.geometry("800x500+0+0")
        self.root.config(bg="#060505")

        self.file_path = 'archivo.txt'
        self.archivo_texto = StringVar()
        self.archivo_texto.set(self.read_text_file(self.file_path))

        encabezado = Label(root, text="WPM Speed Test",
                           width=20, font=('arial', 16, 'bold'), bg='#FFC300')
        encabezado.grid(row=0, columnspan=3)

        frame = LabelFrame(self.root, text='Escriba el siguiente texto: ',
                           bg="#FFA262", padx=20, pady=20,)
        frame.grid(row=1, columnspan=3, pady=10, sticky='W')

        # LABELS
        label_text = Label(frame, textvariable=self.archivo_texto,
                          font=('arial', 12, 'bold'), bg="#FFA262")
        label_text.grid(row=2, columnspan=3, sticky='W')

    def read_text_file(self, file_path):
        """
        Lee el contenido de un archivo de texto (.txt) y lo devuelve como una cadena de texto.
        """
        try:
            with open(file_path, "r") as file:
                text = file.read()
                return text
        except FileNotFoundError:
            print("El archivo no existe.")

   
if __name__ == '__main__':
    root = Tk()
    applicaton = SpeedTestWpm(root)
    root.mainloop()
