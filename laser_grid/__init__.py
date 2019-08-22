import display
import math
import htmlcolor
import leds
import buttons

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

def drawVerticalLines(width, widthBottom):
    offsetTop = yOffset + 1
    for i in range(16):
        xPositionTop = width - i * 10
        xPositionBotttom = math.ceil(widthBottom - i * 30)
        if xPositionBotttom >= 0 and xPositionBotttom <= contextWidth:
            disp.line(
                xPositionTop,
                yOffset + 1,
                xPositionBotttom,
                contextHeight,
                col = htmlcolor.MAGENTA
            )
        else:
            adjacent = abs(xPositionBotttom - xPositionTop)
            opposite = contextHeight - offsetTop
            if xPositionBotttom < 80:
                xPosition = 0
                xDiff = abs(0 - xPositionBotttom)
            else: 
                xPosition = contextWidth
                xDiff = abs(contextWidth - xPositionBotttom)
            yPosition = xDiff * (opposite / adjacent)
            disp.line(
                xPositionTop,
                yOffset + 1,
                xPosition,
                math.ceil(contextHeight - yPosition),
                col = htmlcolor.MAGENTA
            )
    disp.update()

def loop():
    ledsOn = True
    while(True):
        for i in range(10):
            pressed = buttons.read(
                buttons.BOTTOM_LEFT | buttons.BOTTOM_RIGHT
            )
            if pressed:
                ledsOn = not ledsOn
            if ledsOn:
                for j in range(13):
                    if i < 6:
                        leds.prep(j, [math.floor(i * 50), 0, math.floor(i * 50)])
                    else: 
                        leds.prep(j, [math.floor(255 - i * 50), 0, math.floor(255 - i * 50)])
            else:
                for j in range(13):
                    leds.prep(j, [0, 0, 0])
            leds.update()
            setUpGrid()
            drawVerticalLines(
                contextWidth - i,
                contextWidth * 2 - i * 3
            )

loop()