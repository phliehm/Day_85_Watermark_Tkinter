'''
1. Show GUI
2. loading image on button click --> show it
3. converting watermark text to an image which can be overlayed
4. doing some maths to the original image and the watermark image
5. show new image
6. save it on click (enter file name)

GUI content:
- Button to select image (file path)
- Text field for watermark text
- window to show image
- apply button for watermark
- save button for image

'''

import tkinter 
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageFont, ImageDraw, ImageGrab
import time
import math




filename = ""
def open_file():
    print(canvas.winfo_height(), canvas.winfo_width())
    global filename
    filename = fd.askopenfilename()
    print(filename)
    photo = ImageTk.PhotoImage(file=filename)
    canvas.config(width=photo.width(),height=photo.height())
    canvas.delete("all") # deletes everything showing on the canvas'
    canvas.create_image(photo.width()/2,photo.height()/2,image = photo)
    canvas.grid(column=0,row=0)
    canvas.image = photo # if this is not done, it wont work, no image will be shown, ChatGPT says its because the image gets garbage collected, not sure why that is the case


def add_watermark():
    print(canvas.winfo_height(), canvas.winfo_width())
    global filename
    
    n = 5 # number of watermarks
    watermark = "Protected"
    watermark = entry_watermark.get()
    with Image.open(filename).convert('RGBA') as base:
        width, height  = base.size
        pad_percentage = 0.1 # padding percentage
        pad = math.floor(width * pad_percentage)    # calculate the gap from the edges to the watermarks
       
        fontsize = math.floor((height-pad*2)/(2*n - 1))    # - 2*margins, 2n-1 lines, n times watermark, n-1 empty lines
        font = ImageFont.truetype("arial.ttf", fontsize)    # set the font
        
        txt_image = Image.new('RGBA',base.size,(255,255,255,0)) # make empty image
        txt = ImageDraw.Draw(txt_image)     # initialise drawing object for the empty image
        text_width = math.floor(txt.textlength(watermark, font=font)) # get the text length
        shift = math.floor((width - 2*pad - text_width)/(n-1)) # shift per text line
        shifts = 0
        print(f"Fontsize: {fontsize}, text width: {text_width}, shift: {shift}")
        for i in range(0 + pad,height-pad-fontsize+1,2*fontsize): # "+1" needed to get correct number of watermarks
            print(i)
            txt.text((pad + shift*shifts, i), watermark, font=font, fill =(255, 255, 255,100)) # new text for each line, shifted
            shifts += 1
        combined = Image.alpha_composite(base,txt_image)
        canvas.delete("all") # deletes everything showing on the canvas'
        photo = ImageTk.PhotoImage(combined)
        canvas.create_image(photo.width()/2 ,photo.height()/2,image = photo, anchor='center')
        canvas.grid(column=0,row=0)
        canvas.image = photo
        #combined.show()


def save_image():
    x0 = canvas.winfo_rootx()
    y0 = canvas.winfo_rooty()
    x1 = x0 + canvas.winfo_width()
    y1 = y0 + canvas.winfo_height()
    print(f"Width: {canvas.winfo_width()}, Height: {canvas.winfo_height()}")
    img = ImageGrab.grab(bbox= (x0,y0,x1,y1))
    img.save("Result.png")
    
window = tkinter.Tk() # initialise the tkinter window
window.title("Watermarker")
window.config(padx=50, pady=50)
canvas = tkinter.Canvas(width=800, height=800, bg='black')
canvas.grid(column=0,row=0, columnspan=4)


b_load = tkinter.Button(text="1. Load image", command=open_file)
b_load.grid(column=0, row=3, pady=10, sticky='W')

b_add_watermarks = tkinter.Button(text="3. Apply watermark", command= add_watermark)
b_add_watermarks.grid(column=2,row=3)

l_watermark = tkinter.Label(text="2. Watermark text:")
l_watermark.grid(column=1, row=3, sticky='W')
entry_watermark = tkinter.Entry(width=15)
entry_watermark.grid(column=1, row=3, sticky='E')

b_save_new_image = tkinter.Button(text="4. Save new image", command=save_image)
b_save_new_image.grid(column=3, row=3, sticky='E')

window.mainloop() # run the mainloop, keep the window open