#!/usr/env python

class Duck:
    def quack(self):
        print "Duck.duck..duck..."

    def swim(self):
        print "I am a duck, I can swim"

    def fly(self):
        print "I am a duck,I can fly"

    def display(self):
        pass

class Mallardduck(Duck):
	def display(self):
		print "I am a Green head duck..."

class RedheadDuck(Duck):
	def display(self):
		print "I am a Red head duck..."

class RubberDuck(Duck):
	def display(self):
		print "I am a rubberduck"
	def fly(self):
		print "I can't fly"

if __name__=="__main__":
    duck=Duck()
    duck.quack()
    duck.swim()
    duck.fly()

    mallarduck=Mallardduck()
    mallarduck.display()
    mallarduck.fly()
    mallarduck.swim()
    mallarduck.quack()

    rhduck=RedheadDuck()
    rhduck.display()
    rhduck.quack()
    rhduck.swim()
    rhduck.fly()
    
    rbduck=RubberDuck()
    rbduck.display()
    rbduck.quack()
    rbduck.swim()
    rbduck.fly()
