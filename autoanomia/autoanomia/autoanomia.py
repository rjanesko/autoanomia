from os import chdir
from PIL import Image, ImageOps, ImageFont, ImageDraw
import random
import textwrap
from pathlib import Path, PurePath

#chdir('/autoanomia')

#paths
#home=Path.home()
p=Path.cwd()
fontSource = p.joinpath('acre-medium.otf')
print('working directory:')
print(Path.cwd())
print(Path.home())
print(p)
print(p.joinpath('acre-medium.otf'))


#text variables
positions = [(350,250), (850,250), (1350,250), (1850,250),(350,950),(850,950),(1350,950),(1850,950)]
#testString="ABCDEFGHIJKL"

size=60
#font = ImageFont.truetype('C:\coding\python\\autoanomia\\acre-medium.otf',size)
font = ImageFont.truetype(str(p.joinpath('acre-medium.otf')),size)
fill='black'
anchor='ma'
align='center'
catWidth=8
catMax=15
fontSize=font.getsize('hg')[1]
#io stuff
categories=[]
tooLong=[]

catStream = open(str(p.joinpath('categories.txt')),'r',encoding='utf-8')
catString = catStream.read()
categories=catString.split(',')

#filter longs
for cat in categories:
    if len(cat)>catMax:
        tooLong.append(cat)
        categories.remove(cat)




#randomize order
random.shuffle(categories)

#figures out how many sheets can be printed
sheets=len(categories)//8
    

#open the template and create a drawable version
template = Image.open(str(p.joinpath('template.png')))

drawTemplate = ImageDraw.Draw(template)






def addText(currPosition,text):
    text=textwrap.fill(text,catWidth)
    drawTemplate.multiline_text(currPosition,text,font=font,align=align,anchor=anchor,fill=fill)
    #print (currPosition)

def newInvert(position):
    boxTuple = (position[0]-240,position[1]-50,position[0]+245,position[1]+175)
   
    newPos = (position[0]-250,position[1]+350)
    box = template.crop(boxTuple)
    box = box.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    box = box.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    template.paste(box,newPos)


#loop through categories
catCounter=0
sheetCounter=1
#print(len(categories))       

#this loop controls how many sheets will be printed
for x in range(sheets):
    template = Image.open(str(p.joinpath('template.png')))
    #start new sheet based on template
    drawTemplate = ImageDraw.Draw(template)
    #reset position counter
    positionCounter=0
    #this loop iterates through all card positions
    for x in range(8):
        #add category at catCounter to card position at positionCounter
        addText(positions[positionCounter],categories[catCounter])
        newInvert(positions[positionCounter])
        positionCounter += 1
        catCounter+=1
        #print('sheet done')
    
    template.save(str(p.joinpath(f"output{sheetCounter}.png")))
    sheetCounter+=1

#make leftover list
leftoversList=[]
print(catCounter)
leftoverAmount=len(categories) - catCounter
for x in range(leftoverAmount):
    leftoversList.append(categories[catCounter])
    print(leftoversList)
    if catCounter == len(categories)+1:
        break
    catCounter += 1
    
#leftover i/o
leftovers=open(str(p.joinpath('leftovers.txt')),'w+')
for leftover in leftoversList:
    leftovers.write(f"{leftover}\n")
for longs in tooLong:
    leftovers.write(f'Too long: {longs}\n')
leftovers.close()


