from PIL import Image,ImageFont,ImageDraw
import os

file=open('guests.txt')
n=file.readlines()

for i in n:
    x=i[:-1]
    im = Image.new('RGBA', (288, 360),'white')
    image=Image.open('flowers.png')
    image=image.resize((288,360))
    im.paste(image,(0,0))

    draw=ImageDraw.Draw(im)
    draw.text((8,250),'It would be a pleasure to have the company of',fill='purple')
    draw.text((130,270),x,fill='purple')
    draw.text((39,290),'at 11010 Memory Lane on April 1st',fill='purple')
    draw.rectangle((2,2,285,355),outline='black')

    im.save(f'{x}sinvitation.png')
    
