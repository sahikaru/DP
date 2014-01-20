#!/usr/env python

class Duck:
    def quack(self):
        print "Quack:Duck.duck..duck..."

    def swim(self):
        print "Swim:I am a duck, I can swim"

    def display(self):
        pass

class Mallardduck(Duck):
	def display(self):
		print "Display:I am a Green head duck..."

class RedheadDuck(Duck):
	def display(self):
		print "Display:I am a Red head duck..."

if __name__=="__main__":
    duck=Duck()
    duck.display()
    duck.quack()
    duck.swim()

    mallarduck=Mallardduck()
    mallarduck.display()
    mallarduck.quack()
    mallarduck.swim()

    rhduck=RedheadDuck()
    rhduck.display()
    rhduck.quack()
    rhduck.swim()

