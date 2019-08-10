# CircuitPlaygroundExpress_NeoPixel
 
import time
import random
import touchio
import board
import neopixel
 
pixels = neopixel.NeoPixel(board.D3, 7, brightness=.2)
pixels.fill((0, 0, 0))
pixels.show()

touch_pad = board.A0
touch = touchio.TouchIn(touch_pad)
touch.threshold = touch.threshold + 50

# choose which demos to play
# 1 means play, 0 means don't!
simpleCircleDemo = 0
flashDemo = 0
rainbowDemo = 1
rainbowCycleDemo = 0

# COLORS 
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
ORANGE = (255,165,0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
SKYBLUE = (135,206,250)
PURPLE = (180, 0, 255)
BLACK = (0, 0, 0)
NEARBLACK = (18, 0, 30)
LOWWHITE = (4, 4, 4)
PINK = (255, 51,153)

# COLOR PALLETS
LIGHTNING = [WHITE, CYAN, SKYBLUE, BLUE, PURPLE]
FIRE = [RED, YELLOW, GREEN, ORANGE]
TWILIGHT = [PURPLE, CYAN, BLUE, SKYBLUE, PINK]
PINKISH = [RED, PINK, PURPLE, WHITE]

pixels.fill(PURPLE)
pixels.show()

rStep = 4
gStep = 0
bStep = 6
DIRECTION = 1 # 1 = down 0 = up

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 85:
        # print((int(pos * 3), int(255 - (pos * 3)), 0))
        return (int(pos * 3), int(255 - (pos * 3)), 0)
    elif pos < 170:
        pos -= 85
        # print((int(255 - (pos * 3)), 0, int(pos * 3)))
        return (int(255 - (pos * 3)), 0, int(pos * 3))
    else:
        pos -= 170
        # print((0, int(pos * 3), int(255 - pos * 3)))
        return (0, int(pos * 3), int(255 - pos * 3))
 
def multiPalletBurst(aPixel, aPallet):
    #total duration of burst
    burstDuration = .0625
    
    #how many colors in the pallet?
    numColors = len(aPallet)
    # print('numColors is ', numColors)
    miniBurst = burstDuration/numColors
    # print('  miniBurst is', miniBurst)
    # for total number of colors in pallet, choose a random one
    for i in range(numColors):
        aColor = random.randint(0, numColors-1)
        pixels[aPixel] = aPallet[aColor]
        pixels.show()
        time.sleep(burstDuration/numColors)
 
while True:
    aPixel = pixels[0]
    rCur = aPixel[0]
    gCur = aPixel[1]
    bCur = aPixel[2]
    
    # print("rCur: ", rCur)
    # print("gCur: ", gCur)
    # print("bCur: ", bCur)
    
    if touch.value:
        for i in range(random.randrange(20, 40)):
            aStrike = random.randrange(7)
            multiPalletBurst(aStrike, PINKISH)
        
    if (rCur <= 18 or bCur <= 30):
        for i in range(0, 7):
            pixels[i] = NEARBLACK
        DIRECTION = 0
        # print("GOING UP")
    
    if (rCur >= 180 or bCur >= 255):
        for i in range(0, 7):
            pixels[i] = PURPLE
        DIRECTION = 1
        # print("GOING DOWN")
    
    if DIRECTION == 1:
        # for i in range(0, 7):
        #     pixels[i] = ((rCur - rStep),(gCur - gStep),(bCur - bStep))
        pixels.fill(((rCur - rStep),(gCur - gStep),(bCur - bStep)))
        pixels.show()

    if DIRECTION == 0:
        # for i in range(0, 7):
        #     pixels[i] = ((rCur + rStep),(gCur + gStep),(bCur + bStep))
        pixels.fill(((rCur + rStep),(gCur + gStep),(bCur + bStep)))
        pixels.show()
        
    #time.sleep(.1)