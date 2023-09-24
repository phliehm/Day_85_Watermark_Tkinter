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
from PIL import Image, ImageTk, ImageFont, ImageDraw
import time
import math



filename = ""
def open_file():
    global filename
    filename = fd.askopenfilename()
    print(filename)
    photo = ImageTk.PhotoImage(file=filename)
    canvas.config(width=photo.width(),height=photo.height())
    canvas.delete("all") # deletes everything showing on the canvas'
    canvas.create_image(photo.width()/2+1,photo.height()/2+1,image = photo)
    canvas.grid(column=0,row=0)
    canvas.image = photo # if this is not done, it wont work, no image will be shown, ChatGPT says its because the image gets garbage collected, not sure why that is the case

  


def add_2_images():
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
        canvas.create_image(photo.width()/2 + 1,photo.height()/2 + 1,image = photo)
        canvas.grid(column=0,row=0)
        canvas.image = photo
        #combined.show()


# 1. 10% from edge away
# 2. calculate font size
# 3. calculate how many lines possible
# 4. draw the text multiple times always shifted a bit to the right so it ends up 10% from the right    

window = tkinter.Tk() # initialise the tkinter window
window.title("Watermarker")
window.config(padx=50, pady=50)
canvas = tkinter.Canvas(width=800, height=800, bg='black')
canvas.grid(column=0,row=0, columnspan=3)

b_load = tkinter.Button(text="Load image", command=open_file)
b_load.grid(column=3, row=3)

b_add_2_images = tkinter.Button(text="Apply watermark", command= add_2_images)
b_add_2_images.grid(column=1,row=3)

l_watermark = tkinter.Label(text="Watermark text:")
l_watermark.grid(column=0, row=3, sticky='W')
entry_watermark = tkinter.Entry()
entry_watermark.grid(column=0, row=3, sticky='E')

window.mainloop() # run the mainloop, keep the window open