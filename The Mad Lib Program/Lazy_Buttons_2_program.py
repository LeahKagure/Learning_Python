# Lazy Buttons 2
# Demonstrates using a class with tkinter

from tkinter import *


class Application(Frame):
    """A GUI application with three buttons."""
    def __init__(self, master):
        """Initialize the Frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create three buttons that do nothing."""
        # Create first button
        self.bttn1 = Button(self, text="I do nothing!")
        self.bttn1.grid()

        # Create second button
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text="Me too!")

        # Create third button
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Same here!"


# Main
root = Tk()
root.title("Lazy Buttons 2")
root.geometry("200x85")

app = Application(root)
root.mainloop()
