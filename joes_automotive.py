##
# --Joe's Automotive Shop Calculator--
# By Parker Jolly
# 11/19/2025
# Description: A program to calculate costs for Joe's repair shop
# Notes: None
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
       self.main_window.title("Joe's Automotive Repair Shop")

       # Call the other init functions
       self.__setup_labelframe()
       self.__setup_checkframe()
       self.__setup_buttonframe()

       #Enter the main loop
       tk.mainloop()

    def __setup_labelframe(self):
        # Create the top label frame
        self.entryframe1 = tk.Frame(self.main_window)

        # Create the label
        self.toplabel = tk.Label(self.entryframe1, text="Select the options you want:")
    
        # Pack
        self.toplabel.pack(side="top")
        self.entryframe1.pack()

    def __setup_checkframe(self):
        # Create the checkbox frame
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
        self.oilchangecheckbox =          tk.Checkbutton(self.checkboxframe,text="Oil Change | $30",          variable=self.oilchangecheckboxvariable)
        self.lubejobcheckbox =            tk.Checkbutton(self.checkboxframe,text="Lube Job | $20",            variable=self.lubejobcheckboxvariable)
        self.radiatorflushcheckbox =      tk.Checkbutton(self.checkboxframe,text="Radiator Flush | $40",      variable=self.radiatorflushcheckboxvariable)
        self.transmissionfluidcheckbox =  tk.Checkbutton(self.checkboxframe,text="Transmission Fluid | $100",  variable=self.transmissionfluidcheckboxvariable)
        self.inspectioncheckbox =         tk.Checkbutton(self.checkboxframe,text="Inspection | $35",          variable=self.inspectioncheckboxvariable)
        self.mufflerreplacementcheckbox = tk.Checkbutton(self.checkboxframe,text="Muffler replacement | $200", variable=self.mufflerreplacementcheckboxvariable)
        self.tirerotationcheckbox =       tk.Checkbutton(self.checkboxframe,text="Tire Rotation | $20",       variable=self.tirerotationcheckboxvariable)

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
        # init
        total = 0

        # If the button is checked, its 1, otherwise, its 0. So 30*0 = +0, but 30*1 = +30
        total += self.oilchangecheckboxvariable.get()          * 30
        total += self.lubejobcheckboxvariable.get()            * 20
        total += self.radiatorflushcheckboxvariable.get()      * 40
        total += self.transmissionfluidcheckboxvariable.get()  * 100
        total += self.inspectioncheckboxvariable.get()         * 35
        total += self.mufflerreplacementcheckboxvariable.get() * 200
        total += self.tirerotationcheckboxvariable.get()       * 20

        # Display total
        messagebox.showinfo("Total",f"Your total is ${total}")
       
        
if __name__ == "__main__":
    # Call main function
    main()