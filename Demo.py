import Card
import Game
import time
import RPi.GPIO as GPIO

newCard = Card.Card()
newGame = Game.SnakeGame()

redLed = 26
greLed = 16

# setting up the LED
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(redLed, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(greLed, GPIO.OUT, initial = GPIO.LOW)

print "Tap the card to start playing!!!\n"

newCard.GetCard()

print "\nHello %s, your highest score in Snake is %d\n" \
%(newCard.name, newCard.score)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(greLed, GPIO.OUT)
GPIO.output(redLed, GPIO.LOW)
GPIO.output(greLed, GPIO.HIGH)

print "\nStart to play snake\n"
time.sleep(1)

newGame.playgame()

print "\nTap the card to update the score"
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(greLed, GPIO.OUT)
GPIO.output(redLed, GPIO.HIGH)
GPIO.output(greLed, GPIO.LOW)

newCard.UpdateScore(newGame.score)
newCard.WriteCard()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(greLed, GPIO.OUT)
GPIO.output(redLed, GPIO.LOW)
GPIO.output(greLed, GPIO.HIGH)

print "\nThank you for playing"
