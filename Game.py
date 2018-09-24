#import
from evdev import InputDevice, categorize, ecodes
import Matrix
import time
from random import randint

aBtn = 289
bBtn = 290
xBtn = 288
yBtn = 291

lTrig = 292
rTrig = 293

#Y, B, A, X
DRECT = [(-1, 0), (0, 1), (1, 0), (0, -1)]

SPEED = 1000

class SnakeGame:
    score = 0

    gamepad = None
    newmatrix = None

    snakeLen = 1
    snakePos = [(0, 0)]

    bait = (3, 3)

    direct = (0, 0)

    def __init__(self):
        self.gamepad = InputDevice('/dev/input/event0')
        self.newmatrix = Matrix.Matrix()

    def playgame(self):
        count = 0
	self.newmatrix.ShowMsg("Start playing SNAKEEEE")
        while True:
            for event in self.gamepad.active_keys():
                if event == yBtn:
                    if self.direct != DRECT[2] or self.snakeLen < 3:
		        self.direct = DRECT[0]
                elif event == bBtn:
		    if self.direct != DRECT[3] or self.snakeLen < 3:
                        self.direct = DRECT[1]
                elif event == aBtn:
                    if self.direct != DRECT[0] or self.snakeLen < 3:
		        self.direct = DRECT[2]
                elif event == xBtn:
                    if self.direct != DRECT[1] or self.snakeLen < 3:
		        self.direct = DRECT[3]
            if count == SPEED:
                if self.checkLose():
		    self.score = self.snakeLen
		    for i in range(2):
		        self.newmatrix.ShowMsg("You lose!! Your score is %d"\
 %(self.score))		
			print "\n\nYou lose!! Your score is %d\n\n"%(self.score)
		    break
		else:
		    self.checkState()
                    self.Display()
            count = (count + 1) % (SPEED + 1)

    def Display(self):
        image = [[0 for x in range(8)] for y in range(8)]
        for dot in self.snakePos:
            image[dot[0]][dot[1]] = 1
        image[self.bait[0]][self.bait[1]] = 1
        self.newmatrix.DisplayImage(image)

    def checkState(self):
        if self.snakePos[0] == self.bait:
            tmp = self.snakePos[self.snakeLen - 1]
	    self.snakeLen += 1
            self.snakePos.append(tmp)
            for i in range(self.snakeLen-1, 0, -1):
		self.snakePos[i] = self.snakePos[i - 1]
	    self.snakePos[0] = ((self.snakePos[0][0] + self.direct[0]) % 8,\
(self.snakePos[0][1] + self.direct[1]) % 8)
	    while self.checkBait():
                self.bait = (randint(0, 7), randint(0, 7))
        else:
	    for i in range(self.snakeLen-1, 0, -1):
		self.snakePos[i] = self.snakePos[i - 1]
            self.snakePos[0] = ((self.snakePos[0][0] + self.direct[0]) % 8,\
(self.snakePos[0][1] + self.direct[1]) % 8)

    def checkBait(self):
        for dot in self.snakePos:
            if self.bait == dot:
                return True
        return False

    def checkLose(self):
	for i in range(1, self.snakeLen):
	    if self.snakePos[i] == self.snakePos[0]:
		return True
	return False

