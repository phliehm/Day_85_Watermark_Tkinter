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
from PIL import Image, ImageTk
import time

filename = ""
def open_file():
    global filename
    filename = fd.askopenfilename()
    print(filename)
    photo = ImageTk.PhotoImage(file=filename)
    canvas.delete("all") # deletes everything showing on the canvas
    canvas.create_image(100,100,image = photo)
    canvas.grid(column=0,row=0)
    canvas.image = photo # if this is not done, it wont work, no image will be shown, ChatGPT says its because the image gets garbage collected, not sure why that is the case
    


window = tkinter.Tk() # initialise the tkinter window
test_image = ImageTk.PhotoImage(file="D:/Coding/1_LearnPython/1_100Days_of_Python/38_Render_Html_webpage/static/images/pic09.jpg")
window.title("Watermarker")
canvas = tkinter.Canvas(width=800, height=800)
canvas.create_image(500,200,image=test_image)
canvas.grid(column=0,row=0)

b_load = tkinter.Button(text="Load image", command=open_file)
b_load.grid(column=3, row=3)
window.mainloop() # run the mainloop, keep the window open