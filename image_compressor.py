import PIL
from PIL import Image
from tkinter.filedialog import *

file = askopenfilename()

img = PIL.Image.open(file)

height , width = img.size

img = img.resize((height,width), PIL.Image.ANTIALIAS)

save = asksaveasfilename()

img.save(save+"_compressed.JPG")
