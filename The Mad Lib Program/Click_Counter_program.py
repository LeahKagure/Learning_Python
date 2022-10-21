# Click Counter
# Demonstrates binding an event with an event handler

from tkinter import *


class Application(Frame):
    """GUI application which counts button clicks."""
    def __init__(self, master):
        """Initializes the frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0        # The number of button clicks
        self.create_widget()

    def create_widget(self):
        """Create button which displays number of clicks."""
        self.bttn = Button(self)
        self.bttn["text"] = "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        """Increases click count and display new total."""
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)


# Main
root = Tk()
root.title("Click Counter")
root.geometry("200x50")

app = Application(root)

root.mainloop()
