##
# --Long-distance Call Calculator--
# By Parker Jolly
# 11/19/2025
# Description: A program to calculate costs for a call
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
       self.main_window.title("Call Cost Calculator (CCC)")

       # Call the other init functions
       self.__setup_entryframe()
       self.__setup_radiobuttonframe()
       self.__setup_buttonframe()

       #Enter the main loop
       tk.mainloop()

    def __setup_entryframe(self):
        # Create the top label/entry frame
        self.entryframe = tk.Frame(self.main_window)

        # Create the label and entrybox
        self.label = tk.Label(self.entryframe, text="Enter the length of the call in minutes, then select the time below:")
        self.entrybox = tk.Entry(self.entryframe)
    
        # Pack
        self.label.pack(side="left")
        self.entrybox.pack(side="right")
        self.entryframe.pack()

    def __setup_radiobuttonframe(self):
        # Create the radiobutton frame
        self.radiobuttonframe = tk.Frame(self.main_window)

        # Create and initilize variable
        self.radiobuttonsvar = tk.IntVar()
        self.radiobuttonsvar.set(1)

        # Create the Radiobuttons
        self.daytimeRadioButton =  tk.Radiobutton(self.radiobuttonframe,text="Daytime (6:00 A.M. through 5:59 P.M.)",   variable=self.radiobuttonsvar, value=1)
        self.eveningRadioButton =  tk.Radiobutton(self.radiobuttonframe,text="Evening (6:00 P.M.  through 11:59 P.M.)", variable=self.radiobuttonsvar, value=2)
        self.offPeakRadioButton =  tk.Radiobutton(self.radiobuttonframe,text="Off-Peak (midnight through 5:59 P.M.) ",  variable=self.radiobuttonsvar, value=3)
        

        # Pack
        self.daytimeRadioButton.pack()
        self.eveningRadioButton.pack()
        self.offPeakRadioButton.pack()
        self.radiobuttonframe.pack()

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

        # Get which radiobutton we selected and set rate
        if self.radiobuttonsvar.get() == 1:
            rate = 0.02
        elif self.radiobuttonsvar.get() == 2:
            rate = 0.12
        else:
            rate = 0.05

        # Display total or error
        try:
            messagebox.showinfo("Total",f"Your total is ${rate*float(self.entrybox.get()):.2f}")
        except:
            messagebox.showinfo("Error","Invalid input",icon="warning")
       
        
if __name__ == "__main__":
    # Call main function
    main()

    