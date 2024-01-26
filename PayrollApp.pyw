import datetime
import getpass
import os
import re
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from ReformatXeroFile import convertXero

PADL = 30  # padding left

# global variable to save path taken from view for xero file
xeroPath = ''

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.addWidgets()

    def addWidgets(self):
        self.xeroLabel = tk.Label(self.master, text="Select xero file you want to reformat: ")
        self.xeroLabel.place(x=PADL, y=30)

        self.xeroButton = ttk.Button(self.master, text="Browse", command=self.open_file)
        self.xeroButton.place(x=PADL, y=60)

        self.convertButton = ttk.Button(self.master, text="Convert File", command=self.convertFile)
        self.convertButton.pack(side="bottom", pady=20)

    def open_file(self):
        global xeroPath
        file_path = filedialog.askopenfilename()
        if file_path:
            self.xeroLabel.config(text=str(file_path))
            xeroPath = file_path

    def convertFile(self):
        try:
            with open(xeroPath, 'r') as file:
                # store the outputs
                outputs = []

                # process each block
                for line in file:
                    output = convertXero(line.strip())
                    outputs.append(output)


                # write outputs to txt file
                    currentDate = datetime.datetime.now()
                    date = datetime.datetime.strftime(currentDate, '%d%m%Y')
                    outputFilePath = 'C:\\Users\\' + getpass.getuser() + '\\Downloads\\import' + date + 'SantanderFile.txt'

                with open(outputFilePath, 'w') as outputFile:
                    for output in outputs:
                        if(output!= ""):
                            outputFile.write(output + '\n')
                messagebox.showinfo("Complete", f"File conversion completed. Converted file saved to: {outputFilePath}")
                
        except FileNotFoundError:
            messagebox.showerror("Error", f"File not found: {xeroPath}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error occurred: {e}")

root = tk.Tk()
root.title("Payroll Convert App")
root.geometry("500x350")
app = Application(master=root)
app.mainloop()
