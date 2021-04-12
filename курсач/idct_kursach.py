import numpy as np
import PIL.Image
from scipy import fft
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
import matplotlib.pylab as plt



def callback():
    name = fd.askopenfilename()
    img = PIL.Image.open(name).convert('RGBA')
    arr = np.array(img)
    shape = arr.shape
    flat_arr = arr.ravel()
    global vector
    vector = np.matrix(flat_arr)
    print(vector)
    #a = fft.dct(vector)
    #print(a)
    gfg = fft.idct(vector)
    print(gfg)
    im = PIL.Image.fromarray(gfg).convert('RGB')
    im.save("5.png")
    im.show()

errmsg = 'Error!'
root = Tk()
root.geometry("400x300")
tk.Button(text='IDCT', command=callback).pack(fill=tk.X)

root.mainloop()
    
    
