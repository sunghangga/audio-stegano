from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import tkinter
import winsound
import glob
from PIL import Image, ImageTk

    
root = tkinter.Tk()

def ica(X):
    None


def sca(X):
    None

def write_wav(fs_1, S_, method, file_name, write_wav=True):
    None

# create blank tabel
def blank(i,j):
	enter = tkinter.Label(root)
	enter.grid(column=i,row=j)

def browse():
    file_dialog = tkinter.Tk()
    file_dialog.withdraw()
    global file_name
    file_name = filedialog.askopenfilename(initialdir = "/",title = "Select File",filetypes = (("wav file","*.wav"),("all files","*.*")))
    
    split_file_name = file_name.split("/")
    input_browse.delete(0, END)
    # print file wave
    input_browse.insert(1,(split_file_name[len(split_file_name)-1]))

def go(getDropdown):
    None

# play music in destination folder
def play_music(wav_name):
	winsound.PlaySound("../results/separates_audio/"+wav_name,winsound.SND_FILENAME|winsound.SND_ASYNC)

# stop music in destination folder
def stop_music(wav_name):
	winsound.PlaySound(None, winsound.SND_FILENAME|winsound.SND_ASYNC)

# create tabel
def tabel_isi(baris,no,filename,jenis):
    None

def tab_1():
    # create field input
    column = 0
    row = 0
    labelFrame = LabelFrame(tab1, text = "Path Input")
    labelFrame.grid(column = column, row = row, padx = 8, pady = 4, sticky = 'W')
    label = Label(labelFrame, text = "Text File:")
    label.grid(column = column, row = row, sticky = 'W')
    input_text = Entry(labelFrame, width = 30)
    input_text.grid(column = column+1, row = row)
    btn_browse = Button(labelFrame, text = "Browse", command=browse, bg="blue")
    btn_browse.grid(column = column+2, row = row)
    label2 = Label(labelFrame, text = "Image File:")
    label2.grid(column = column, row = row+1, sticky = 'W')
    input_img = Entry(labelFrame, width = 30)
    input_img.grid(column= column+1, row = row+1)
    btn_browse = Button(labelFrame, text = "Browse", command=browse, bg="blue")
    btn_browse.grid(column = column+2, row = row+1)
    label3 = Label(labelFrame, text = "Audio File:")
    label3.grid(column = column, row = row+2, sticky = 'W')
    input_wav = Entry(labelFrame, width = 30)
    input_wav.grid(column= column+1, row = row+2)
    btn_browse = Button(labelFrame, text = "Browse", command=browse, bg="blue")
    btn_browse.grid(column = column+2, row = row+2)
    label4 = Label(labelFrame, text = "Destination Path:")
    label4.grid(column = column, row = row+3, sticky = 'W')
    input_dest = Entry(labelFrame, width = 30)
    input_dest.grid(column= column+1, row = row+3)
    btn_browse = Button(labelFrame, text = "Browse", command=browse, bg="blue")
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

    btn_embed = Button(tab1, text = "Embed", command=browse, bg="green")
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
root.minsize(600, 400)

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


# #membuat combo box
# tabel = tkinter.Label(root,text = "METODE")
# tabel.place(x=403, y=0)

# comboExample = ttk.Combobox(root, 
#                             values=[
#                                     "ICA", 
#                                     "SCA"])
# # comboExample.grid(row=baris+1, column=baris)
# comboExample.place(x=457,y=0)
# comboExample.current(0)
# # print(comboExample.current(), comboExample.get())

# #membuat tombol go
# btn_browse = tkinter.Button(root, text = "SEPARATE", 
#     command=lambda: go(comboExample.get()))
# btn_browse.place(x=255,y=0)

# blank(baris+1,0)
# #membuat tabel header
# tabel = tkinter.Label(root,text = "NO")
# tabel.grid(row=baris+2, column=0)

# tabel = tkinter.Label(root,text = "FILENAME")
# tabel.grid(row=baris+2, column=1)

# tabel = tkinter.Label(root,text = "PLAYER")
# tabel.grid(row=baris+2, column=2)

# tabel = tkinter.Label(root,text = "MUSIC")
# tabel.grid(row=baris+2, column=3)

# tabel = tkinter.Label(root,text = "TYPE")
# tabel.grid(row=baris+2, column=4)

# tabel_isi(baris+3,"","","")#buat tabel pertama untuk display aja


root.mainloop()
