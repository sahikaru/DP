#!/usr/env python


class Flyable:
    def fly(self):
        pass

class Quackable(object):
    def quack(self):
        pass

class ReadHeadDuckFly(Flyable):
    def fly(self):
        print "I am a readheadduck, I can fly"

class ReadHeadDuckQack(Quackable):
    def quack(self):
        print "I am a readheadduck,Dcuk duck duck..."

class Duck():
    def swim(self):
        print "I am a duck,I can swim..."

class ReadHeadDuck(Duck):
    def __init__(self,flyable,quackable):
        self.f = flyable
        self.q = quackable

    def fly(self):
        return self.f.fly()
    def quack(self):
        return self.q.quack()

class Mallardduckflyable(Flyable):
    def fly(self):
        print "I am a Mallardduck....,I can fly"

class MallardduckQuackble(Quackable):
    def quack(self):
        print "I am a Mallardduck,Duck.duck..duck.."

class Mallardduck(Duck):
    def __init__(self,flyable,quackable):
        self.f = flyable
        self.q = quackable

    def fly(self):
        return self.f.fly()

    def quack(self):
        return self.q.quack()

if __name__ == "__main__":
    duck = Duck()
    duck.swim()
    
    rhduck = ReadHeadDuck(ReadHeadDuckFly(),ReadHeadDuckQack())
    rhduck.fly()
    rhduck.swim()
    rhduck.quack()

    md = Mallardduck(Mallardduckflyable(),MallardduckQuackble())
    md.fly()
    md.quack()
    md.swim()
