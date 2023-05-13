import os
from tkinter import filedialog as fd
from tkinter import *
from PyPDF2 import PdfMerger
from datetime import datetime
import shutil
print(datetime.now())
thispath = os.getcwd()
print(os.getcwd())


def browseFiles():
    file = fd.askopenfilenames(parent=window, title='Pilih File')
    print(file)
    wkspFldr = os.path.dirname(os.path.abspath(file[0]))
    pdfs = file
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(os.getcwd()+"\\result.pdf")
    if(os.path.exists(wkspFldr + "\\result.pdf")):
        os.remove(wkspFldr + "\\result.pdf")
    shutil.move(os.getcwd()+"\\result.pdf", wkspFldr +
                "\\", ".pdf")
    os.system('start "" /max '+wkspFldr + "\\result.pdf")
    merger.close()
    window.destroy()


window = Tk()
window.title('Merge PDF')
window.geometry("500x500")
window.config(background="white")
label_file_explorer = Label(window,
                            text="Merge PDF",
                            width=80, height=4,
                            fg="blue")
button_explore = Button(window,
                        text="Browse Files",
                        command=browseFiles)
button_exit = Button(window,
                     text="Exit",
                     command=exit)
label_file_explorer.grid(column=1, row=1)
button_explore.grid(column=1, row=2)
button_exit.grid(column=1, row=3)
window.mainloop()
