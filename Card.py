#!/usr/bin/env python
# This is the simple card reader

import RPi.GPIO as GPIO
import SimpleMFRC522

class Card:
    id = None
    text = None
    name = ""
    score = 0

    reader = None

    def __init__(self):
        self.reader = SimpleMFRC522.SimpleMFRC522()

    def GetCard(self):
        print "Tap the card to get inforamtion"
        try:
            self.id, self.text = self.reader.read()
	    if not(self.IsRegistered()):
		print "You have to register your ID"
		self.name = raw_input("What is your name? ")
		self.score = 0
	    	self.WriteCard()
	    self.ProcessTheText()
            #print self.id
	    #print self.name
	    #print self.score
	    #print self.text
	finally:
	    pass

    def ProcessTheText(self):
	splitted = self.text.split(',')
	if len(splitted) >= 3:
	    self.name = splitted[1]
            self.score = int(splitted[2])

    def UpdateScore(self, score):
	if score > self.score:        
	    self.score = score

    def WriteCard(self):
        print "Tap to UPDATE your information"
        try:
            text = "yes," + self.name + ',' + str(self.score)
            self.reader.write(text)
            print("Updated")
        finally:
            GPIO.cleanup()
	
    def IsRegistered(self):
	return self.text.split(',')[0] == "yes"
