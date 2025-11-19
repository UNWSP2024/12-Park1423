##
# --MPG Calculator--
# By Parker Jolly
# 11/19/2025
# Description: A program to calculate Miles Per Gallon using tkinter
# Notes: https://www.youtube.com/watch?v=dQw4w9WgXcQ
##

import tkinter as tk
import tkinter.messagebox as messagebox

# Call main and create the GUI
def main():
    window = GUI()

class GUI:

    def __init__(self):
       # Create main window
       self.main_window = tk.Tk()

       # Call the other init functions
       self.__setup_entryframe1()
       self.__setup_entryframe2()
       self.__setup_buttonframe()

       #Enter the main loop
       tk.mainloop()

    def __setup_entryframe1(self):
        # Create the top entry frame
        self.entryframe1 = tk.Frame(self.main_window)

        # Create the top label and entry box
        self.toplabel = tk.Label(self.entryframe1, text="Enter how many gallons of gas your tank holds: ")
        self.entrybox1 = tk.Entry(self.entryframe1)
        
        # Pack
        self.toplabel.pack(side="left")
        self.entrybox1.pack(side="right")
        self.entryframe1.pack()

    def __setup_entryframe2(self):
        # Create the bottom entry frame
        self.entryframe2 = tk.Frame(self.main_window)

        # Create the bottom label and entry box
        self.bottomlabel = tk.Label(self.entryframe2, text="Enter how many miles can be driven on a full tank: ")
        self.entrybox2 = tk.Entry(self.entryframe2)
        
        # Pack
        self.bottomlabel.pack(side="left")
        self.entrybox2.pack(side="right")
        self.entryframe2.pack()

    def __setup_buttonframe(self):
        # Create the button frame
        self.bottomframe = tk.Frame(self.main_window)

        # Create the buttons
        self.calculate_button = tk.Button(self.bottomframe, text="Calculate MPG",command=self.calculate_mpg)
        self.quit_button = tk.Button(self.bottomframe, text="Quit",command=self.main_window.destroy)

        # Pack
        self.calculate_button.pack(side="left")
        self.quit_button.pack(side="right")
        self.bottomframe.pack()

    def calculate_mpg(self):
        
       
        try:
            # Try to convert the text in the upper entry box to a number
            max_gas = None
            max_gas = float(self.entrybox1.get())
        except ValueError: # Handle errors with error messages
            messagebox.showinfo("ERR","Max gas must be a number")
        except:
            messagebox.showinfo("ERR","Invalid input")

        try:
            # Try to convert the text in the lower entry box to a number
            max_miles = None
            max_miles = float(self.entrybox2.get())
        except ValueError: # Handle errors with error messages
            messagebox.showinfo("ERR","Miles driven must be a number",icon="warning")
        except:
            messagebox.showinfo("ERR","Invalid input",icon="warning")

        try:
            # Try to display the result, but if one of them errored and wasnt set properly, do nothing.
            messagebox.showinfo("Result",f"Your milage is {max_miles/max_gas:.2f}")
        except:
            # Do nothing
            pass


if __name__ == "__main__":
    # Call main function
    main()