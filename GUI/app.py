from tkinter import (
    Tk,
    Label,
    Canvas
)

class App:
    def __init__(self, root):
        self.canvas = Canvas(
            root,
            width=600,
            height=500,
            bg='#f9f4e3',

        )
        self.canvas.pack()
        pass

raiz = Tk()
app = App(raiz)
raiz.resizable('false', 'false')
raiz.title('SGD')
raiz.mainloop()
