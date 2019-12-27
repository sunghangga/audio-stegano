from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import tkinter

import os
import time
import wave
import cv2
import testing as Test
import wavelet as Compress
import text_to_image as Tti
import image_to_wav as Itw
from use_aes import UseAES

    
root = tkinter.Tk()
def browse(file, input_file):
    if file == "img":
        name_filetype = "BMP file"
        filetype = "*.bmp"
    else:
        name_filetype = "WAV file"
        filetype = "*.wav"

    file_name = filedialog.askopenfilename(initialdir = "/",title = "Select File",filetypes = ((name_filetype,filetype),("All files","*.*")))

    input_file.delete(0, END)
    input_file.insert(END, file_name)

def browse_dir(input_file):
    input_file.delete(0, END)
    fileopen = filedialog.askdirectory()
    input_file.insert(END, fileopen)

def create_dir(input_dest):
    os.makedirs(os.path.dirname(input_dest.get()+"/PySteg/encrypt/text/"), exist_ok=True)
    os.makedirs(os.path.dirname(input_dest.get()+"/PySteg/encrypt/image/"), exist_ok=True)
    os.makedirs(os.path.dirname(input_dest.get()+"/PySteg/encrypt/audio/"), exist_ok=True)
    os.makedirs(os.path.dirname(input_dest.get()+"/PySteg/decrypt/text/"), exist_ok=True)
    os.makedirs(os.path.dirname(input_dest.get()+"/PySteg/decrypt/image/"), exist_ok=True)
    os.makedirs(os.path.dirname(input_dest.get()+"/PySteg/decrypt/audio/"), exist_ok=True)
    os.makedirs(os.path.dirname(input_dest.get()+"/PySteg/testing/mse/"), exist_ok=True)
    os.makedirs(os.path.dirname(input_dest.get()+"/PySteg/testing/psnr/"), exist_ok=True)

def encrypt_file(input_text,input_img,input_wav,input_dest,level_compress,password):
    create_dir(input_dest)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    '''encrypt message (message, path of plaintext, path of chipertext)'''
    UseAES(password.get()).to_encryption(input_text.get(), input_dest.get()+"/PySteg/encrypt/text/"+timestr+"_plaintext.txt", input_dest.get()+"/PySteg/encrypt/text/"+timestr+"_chippertext.txt")
    '''haar wavelet (level, path of original image, path output image, write, show)'''
    Compress.wavelet_image(int(level_compress.get()), input_img.get(), input_dest.get()+"/PySteg/encrypt/image/"+timestr+"_compress.bmp", True, False)
    '''LSB text to image (key, pathOriginalImage, pathChiperText, pathDestinationImage)'''
    Tti.encrypt(password.get(), input_dest.get()+"/PySteg/encrypt/image/"+timestr+"_compress.bmp", input_dest.get()+"/PySteg/encrypt/text/"+timestr+"_chippertext.txt", input_dest.get()+"/PySteg/encrypt/image/"+timestr+"_embed.bmp")
    '''LSB image to wav (key, pathOriginalMusic, pathImageEmbbed, pathEmbbedWav)'''
    Itw.encrypt(password.get(), input_wav.get(), input_dest.get()+"/PySteg/encrypt/image/"+timestr+"_embed.bmp", input_dest.get()+"/PySteg/encrypt/audio/"+timestr+"_embed.wav")

def tab_1():
    # create field input
    column = 0
    row = 0
    labelFrame = LabelFrame(tab1, text = "Path Input")
    labelFrame.grid(column = column, row = row, padx = 8, pady = 4, sticky = 'W')
    label = Label(labelFrame, text = "Message:")
    label.grid(column = column, row = row, sticky = 'W')
    input_text = Entry(labelFrame, width = 30)
    input_text.grid(column = column+1, row = row)
    label2 = Label(labelFrame, text = "Image File:")
    label2.grid(column = column, row = row+1, sticky = 'W')
    input_img = Entry(labelFrame, width = 30)
    input_img.grid(column= column+1, row = row+1)
    btn_browse = Button(labelFrame, text = "Browse", command=lambda: browse("img", input_img), bg="blue")
    btn_browse.grid(column = column+2, row = row+1)
    label3 = Label(labelFrame, text = "Audio File:")
    label3.grid(column = column, row = row+2, sticky = 'W')
    input_wav = Entry(labelFrame, width = 30)
    input_wav.grid(column= column+1, row = row+2)
    btn_browse = Button(labelFrame, text = "Browse", command=lambda: browse("wav", input_wav), bg="blue")
    btn_browse.grid(column = column+2, row = row+2)
    label4 = Label(labelFrame, text = "Destination Path:")
    label4.grid(column = column, row = row+3, sticky = 'W')
    input_dest = Entry(labelFrame, width = 30)
    input_dest.grid(column= column+1, row = row+3)
    btn_browse = Button(labelFrame, text = "Browse", command=lambda: browse_dir(input_dest), bg="blue")
    btn_browse.grid(column = column+2, row = row+3)

    column = 0
    row = 4
    labelFrame = LabelFrame(tab1, text = "Setting")
    labelFrame.grid(column = column, row = row, padx = 8, pady = 4, sticky = 'W')
    label = Label(labelFrame, text = "Level Compress: ")
    label.grid(column = column, row = row, sticky = 'W')
    level_compress = Spinbox(labelFrame, from_ = 0, to = 10, width = 3)
    level_compress.grid(column = column+1, row = row, sticky = 'W')
    label2 = Label(labelFrame, text = "Password:")
    label2.grid(column = column, row = row+1, sticky = 'W')
    password = Entry(labelFrame, width = 30)
    password.grid(column= column+1, row = row+1)

    btn_embed = Button(tab1, text = "Embed", command=lambda: encrypt_file(input_text,input_img,input_wav,input_dest,level_compress,password), bg="green")
    btn_embed.grid(column = column, row = row+2)

def tab_2():
    column = 0
    row = 0
    labelFrame = LabelFrame(tab2, text = "Path Input")
    labelFrame.grid(column = column, row = row, padx = 8, pady = 4, sticky = 'W')
    label = Label(labelFrame, text = "Stego File:")
    label.grid(column = column, row = row, sticky = 'W')
    input_stego = Entry(labelFrame, width = 30)
    input_stego.grid(column = column+1, row = row)
    btn_browse = Button(labelFrame, text = "Browse", command=browse, bg="blue")
    btn_browse.grid(column = column+2, row = row)
    
    label4 = Label(labelFrame, text = "Destination Path:")
    label4.grid(column = column, row = row+1, sticky = 'W')
    input_dest = Entry(labelFrame, width = 30)
    input_dest.grid(column= column+1, row = row+1)
    btn_browse = Button(labelFrame, text = "Browse", command=browse, bg="blue")
    btn_browse.grid(column = column+2, row = row+1)

    column = 0
    row = 3
    labelFrame = LabelFrame(tab2, text = "Setting")
    labelFrame.grid(column = column, row = row, padx = 8, pady = 4, sticky = 'W')
    label2 = Label(labelFrame, text = "Password:            ")
    label2.grid(column = column, row = row, sticky = 'W')
    password = Entry(labelFrame, width = 30)
    password.grid(column= column+1, row = row)

    btn_embed = Button(tab2, text = "Extract", command=browse, bg="green")
    btn_embed.grid(column = column, row = row+2)       

def tab_3():
    # create field input
    column = 0
    row = 0
    labelFrame = LabelFrame(tab3, text = "MSE & PSNR")
    labelFrame.grid(column = column, row = row, padx = 8, pady = 4, sticky = 'W')
    label = Label(labelFrame, text = "File 1:")
    label.grid(column = column, row = row, sticky = 'W')
    input_text = Entry(labelFrame, width = 30)
    input_text.grid(column = column+1, row = row)
    btn_browse = Button(labelFrame, text = "Browse", command=browse, bg="blue")
    btn_browse.grid(column = column+2, row = row)
    label2 = Label(labelFrame, text = "File 2:")
    label2.grid(column = column, row = row+1, sticky = 'W')
    input_img = Entry(labelFrame, width = 30)
    input_img.grid(column= column+1, row = row+1)
    btn_browse = Button(labelFrame, text = "Browse", command=browse, bg="blue")
    btn_browse.grid(column = column+2, row = row+1)
    label4 = Label(labelFrame, text = "Destination Path:")
    label4.grid(column = column, row = row+2, sticky = 'W')
    input_dest = Entry(labelFrame, width = 30)
    input_dest.grid(column= column+1, row = row+2)
    btn_browse = Button(labelFrame, text = "Browse", command=browse, bg="blue")
    btn_browse.grid(column = column+2, row = row+2)

    column = 0
    row = 3
    labelFrame = LabelFrame(tab3, text = "Setting")
    labelFrame.grid(column = column, row = row, padx = 8, pady = 4, sticky = 'W')
    label = Label(labelFrame, text = "Type of File:         ")
    label.grid(column = column, row = row, sticky = 'W')
    comboExample = ttk.Combobox(labelFrame,values=["Text","Image","Audio"],width=10)
    comboExample.grid(column=column+1, row = row)
    comboExample.current(0)
    # print(comboExample.current(), comboExample.get())

    btn_embed = Button(tab3, text = "Calculate", command=browse, bg="green")
    btn_embed.grid(column = column, row = row+1)


root.title("PySteg")
root.minsize(355, 265)

#Make the notebook
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text = "Encryption")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text = "Decryption")

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text = "Testing")

tabControl.pack(expan = 1, fill = "both")

tab_1()
tab_2()
tab_3()

root.mainloop()