import pandas as pd
import pdfkit
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import os
import time

root= tk.Tk()
root.title("CSV2PDF-Table")
root.minsize(200,150)
canvas1 = tk.Canvas(root, width = 200, height = 150,  relief = 'flat')
canvas1.pack()

label1 = tk.Label(root, text='CSVtoPDF-Formatter')
label1.config(font=('helvetica', 12))
canvas1.create_window(100, 12.5, window=label1)

label2 = tk.Label(root, text='Type in land name:')
label2.config(font=('helvetica', 10))
canvas1.create_window(100, 50, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(100, 70, window=entry1)

def get():
    filename = askopenfilename(initialdir = '/Desktop',title = 'Select file',filetypes = (('text files','*.txt'),('all files','*.*')))
    a = pd.read_csv(filename, sep="\t", na_filter=False, index_col=1, lineterminator="\n", encoding="utf-8")
    split=os.path.splitext(filename)[0]
    a.to_html(split + '.html', border=0, bold_rows=False, justify='left', encoding='utf-8', index=False, header=True)
    
    landname=entry1.get()
    if not name:
      name=" "

    
    options = { 
      'orientation': "Landscape",
      'page-size': "A4",
      'footer-right': "[page]",
      'header-right': "[date]",
      'header-left': name,
      'encoding': "UTF-8",
    } 
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdfkit.from_file(split+'.html', split+'.pdf', configuration=config, options=options)

button1 = tk.Button(text='Choose File', command=get, bg='black', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(100, 100, window=button1)

root.mainloop()



