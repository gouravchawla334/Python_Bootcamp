
from PIL import Image, ImageDraw, ImageFont

# Import pandas 
import pandas as pd
# Import os
import os

# Create a csv file containing name of all students 
# Save this in the same folder
df = pd.read_csv('sheet.csv')

# font variable contain text font which is printed on certificate
font = ImageFont.truetype('arial.ttf',60)

for index,j in df.iterrows():

    # certificate.jpg is a sample of certificate
    img = Image.open('certificate.jpg')
    draw = ImageDraw.Draw(img)

    # Here we delcare first xy coordinate according to certificate and then select name column from csv file which contain all names
    # fill is RGB color 
    draw.text(xy=(530,365),text='{}'.format(j['name']),fill=(184,134,11),font=font)
    
    # Save this created certificate in pictures folder and name of each certificate is same as in csv file
    img.save('pictures/{}.jpg'.format(j['name']))