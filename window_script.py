
import tkinter as ttk
from tkinter import messagebox as msg
import extractor


# main window definitions
main_window = ttk.Tk()
main_window.geometry('500x270')
main_window.title('batch mp4 telemetry extractor')

# variables declaration and  initializing
path = ttk.StringVar()


# executable functions
def execution():
    #print("source path: " + path.get())
    extractor.extractor(path.get())
    msg.showinfo("Extraction completed", "All telemetry data extracted from files in given path and converted to csv type.\nAll converted files located in downloads folder.")


# window widgets implementing
widgets = []

widgets.append(ttk.Label(main_window, text='Automatic executive application for extracting telemetry data from mp4 file'))
widgets.append(ttk.Label(main_window, text='Attention: netwok connection strongly required!', fg='Red'))
widgets.append(ttk.Label(main_window, text='Insert Folder path:'))
widgets.append(ttk.Entry(main_window, width=45, textvariable=path))
widgets.append(ttk.Button(main_window, text='Run', command=execution))

# window widgets exposure
index = 0
for widgjet in widgets:
    widgjet.grid(row=index, column=0, sticky=ttk.NW)
    index += 1

# widget alignment
widgets[3].focus()

#
main_window.mainloop()