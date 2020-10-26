##Armani Rogers
##CSC-355-2
#colorEffects
# Importing imagechops for using the invert() method 
from PIL import Image, ImageChops, ImageEnhance

# Opening the test image, and saving it's object 
img = Image.open('C:/Users/Armani/Pictures/Mr. Koifsh/DSC_9350.jpeg') 
img = img.resize((4928,3264))

# Passing the image object to invert()   
inv_img = ImageChops.invert(img) 
  
# Displaying the output image 
inv_img.show()
