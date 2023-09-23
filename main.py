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

font = ImageFont.truetype("arial.ttf", 100)

filename = ""
def open_file():
    global filename
    filename = fd.askopenfilename()
    print(filename)
    photo = ImageTk.PhotoImage(file=filename)
    canvas.delete("all") # deletes everything showing on the canvas'
    canvas.create_image(200,200,image = photo)
    canvas.grid(column=0,row=0)
    canvas.image = photo # if this is not done, it wont work, no image will be shown, ChatGPT says its because the image gets garbage collected, not sure why that is the case
    

def show_watermark():
    im = Image.new(mode="RGB", size=(800, 800))
    I1 = ImageDraw.Draw(im)
    I1.text((50, 400), "Watermark", font=font, fill =(50, 50, 50))
    im.show()


window = tkinter.Tk() # initialise the tkinter window
window.title("Watermarker")
window.config(padx=50, pady=50)
canvas = tkinter.Canvas(width=800, height=800, bg='black')
canvas.grid(column=0,row=0)

b_load = tkinter.Button(text="Load image", command=open_file)
b_load.grid(column=3, row=3)

b_show_water_image = tkinter.Button(text="Show Watermark", command=show_watermark)
b_show_water_image.grid(column=0, row=3)
window.mainloop() # run the mainloop, keep the window open