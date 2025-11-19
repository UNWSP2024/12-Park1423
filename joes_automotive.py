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
       self.__setup_labelframe()
       self.__setup_checkframe()
       self.__setup_buttonframe()

       #Enter the main loop
       tk.mainloop()

    def __setup_labelframe(self):
        # Create the top entry frame
        self.entryframe1 = tk.Frame(self.main_window)

        # Create the top label and entry box
        self.toplabel = tk.Label(self.entryframe1, text="Enter how many gallons of gas your tank holds: ")
        self.entrybox1 = tk.Entry(self.entryframe1)
        
        # Pack
        self.toplabel.pack(side="left")
        self.entrybox1.pack(side="right")
        self.entryframe1.pack()

    def __setup_checkframe(self):
        # Create the bottom entry frame
        self.checkboxframe = tk.Frame(self.main_window)

        # Create variables
        self.oilchangecheckboxvariable = tk.IntVar()
        self.lubejobcheckboxvariable = tk.IntVar()
        self.radiatorflushcheckboxvariable = tk.IntVar()
        self.transmissionfluidcheckboxvariable = tk.IntVar()
        self.inspectioncheckboxvariable = tk.IntVar()
        self.mufflerreplacementcheckboxvariable = tk.IntVar()
        self.tirerotationcheckboxvariable = tk.IntVar()

        # Create the checkboxes
        self.oilchangecheckbox = tk.Checkbutton(self.checkboxframe,text="Oil Change")
        self.lubejobcheckbox = tk.Checkbutton(self.checkboxframe,text="Lube Job")
        self.radiatorflushcheckbox = tk.Checkbutton(self.checkboxframe,text="Radiator Flush")
        self.transmissionfluidcheckbox = tk.Checkbutton(self.checkboxframe,text="Transmission Fluid")
        self.inspectioncheckbox = tk.Checkbutton(self.checkboxframe,text="Inspection")
        self.mufflerreplacementcheckbox = tk.Checkbutton(self.checkboxframe,text="Muffler replacement")
        self.tirerotationcheckbox = tk.Checkbutton(self.checkboxframe,text="Tire Rotation",)

        # Pack
        self.oilchangecheckbox.pack()
        self.lubejobcheckbox.pack()
        self.radiatorflushcheckbox.pack()
        self.transmissionfluidcheckbox.pack()
        self.inspectioncheckbox.pack()
        self.mufflerreplacementcheckbox.pack()
        self.tirerotationcheckbox.pack()
        self.checkboxframe.pack()

    def __setup_buttonframe(self):
        # Create the button frame
        self.bottomframe = tk.Frame(self.main_window)

        # Create the buttons
        self.calculate_button = tk.Button(self.bottomframe, text="Calculate Total",command=self.calculate_total)
        self.quit_button = tk.Button(self.bottomframe, text="Quit",command=self.main_window.destroy)

        # Pack
        self.calculate_button.pack(side="left")
        self.quit_button.pack(side="right")
        self.bottomframe.pack()

    def calculate_total(self):
        
        total = 0

        total += int(self.oilchangecheckboxvariable) * 20
        total += int(self.lubejobcheckboxvariable) * 20
        total += int(self.radiatorflushcheckboxvariable) * 20
        total += int(self.transmissionfluidcheckboxvariable) * 20
        total += int(self.inspectioncheckboxvariable) * 20
        total += int(self.mufflerreplacementcheckboxvariable) * 20
        total += int(self.tirerotationcheckboxvariable) * 20

        messagebox.showinfo("Total",f"Your total is ${total}")
       
        
if __name__ == "__main__":
    # Call main function
    main()