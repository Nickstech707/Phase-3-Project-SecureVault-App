# from app.cli import CommandLineInterface

# if __name__ == "__main__":
#     cli = CommandLineInterface()
#     cli.run()



import tkinter as tk
from app.gui import GUI

def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()