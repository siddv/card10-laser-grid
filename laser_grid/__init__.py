import display
import math
import htmlcolor

disp = display.open()
yOffset = 9
contextWidth = 160
contextHeight = 80

def setUpGrid():
    yPosition = 1
    disp.clear(htmlcolor.BLACK)
    disp.rect(0, 0, contextWidth, yOffset + 1, col = htmlcolor.CYAN)
    while yPosition < (contextHeight - yOffset):
        disp.line(
            0,
            yPosition + yOffset,
            contextWidth,
            yPosition + yOffset,
            col = htmlcolor.MAGENTA
        )
        yPosition = math.ceil(yPosition * 1.2)
    disp.update()

def drawVerticalLines(width, widthBottom):
    offsetTop = yOffset + 1
    for i in range(16):
        xposTop = width - i * 10
        xposBotttom = math.ceil(widthBottom - i * 30)
        if xposBotttom >= 0 and xposBotttom <= width:
            disp.line(
                xposTop,
                yOffset + 1,
                xposBotttom,
                contextHeight,
                col = htmlcolor.MAGENTA
            )
        else:
            adjacent = abs(xposBotttom-xposTop)
            opposite = contextHeight - offsetTop
            print(math.degrees(math.atan(opposite / adjacent)))
            if xposBotttom < 80:
                xPos = 0
            else: 
                xPos = contextWidth
            disp.line(
                xposTop,
                yOffset + 1,
                xPos,
                contextHeight,
                col = htmlcolor.MAGENTA
            )
    disp.update()

def loop():
    while(True):
        for i in range(10):
            setUpGrid()
            drawVerticalLines(
                contextWidth - i,
                contextWidth * 2 - i * 3)

loop()