import tkinter as tk
from utils import *
from tkinter.filedialog import askopenfilenames, askopenfilename
import tkinter.messagebox as messagebox

def browseKey():
    global filename_key
    filename_key = askopenfilename(initialdir = "/",
                                title = "Select a Key File",
                                filetypes = (("Software License Key File", "*.key*"), ("all files", "*.*")))
    button_select_key.configure(text="Key Selected")
    return filename_key

def encodeFiles():
    try:
        key = load_key(filename_key)
    except:
        messagebox.showerror(title='Warning', message='no key file selected')
        return

    filenames = askopenfilenames(initialdir = "/",
                                title = "Select Files",
                                filetypes = (("Portable Document Format File", "*.pdf*"), ("all files", "*.*")))
    
    for filename in filenames:
        encrypt_file(filename, key, var_inplace_enc.get())

def decodeFiles():
    try:
        key = load_key(filename_key)
    except:
        messagebox.showerror(title='Warning', message='no key file selected')
        return

    filenames_e = askopenfilenames(initialdir = "/",
                                title = "Select Files",
                                filetypes = (("Portable Document Format File", "*.pdf*"), ("all files", "*.*")))
    
    for filename in filenames_e:
        decrypt_file(filename, key, var_inplace_dec.get())
    


window = tk.Tk()
window.title("PDF Coder")
window.geometry("280x290")



var_inplace_enc = tk.IntVar()
var_inplace_dec = tk.IntVar()



button_select_key = tk.Button(window, text="Select Key File", command=browseKey, width=35, height=5)
button_enc = tk.Button(window, text="Encode", command=encodeFiles, width=20, height=5)
check_inplace_enc = tk.Checkbutton(window, text="In-Place", variable=var_inplace_enc, width=10, height=5)
button_dec = tk.Button(window, text="Decode", command=decodeFiles, width=20, height=5)
check_inplace_dec = tk.Checkbutton(window, text="In-Place", variable=var_inplace_dec, width=10, height=5)



button_select_key.grid(row = 0, column=0, columnspan=2, padx = 5, pady = 5)
button_enc.grid(row = 1, column = 0, padx = 5, pady = 5)
check_inplace_enc.grid(row = 1, column = 1, padx = 5, pady = 5)
button_dec.grid(row = 2, column = 0, padx = 5, pady = 5)
check_inplace_dec.grid(row = 2, column = 1, padx = 5, pady = 5)


window.mainloop()