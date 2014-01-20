#!/usr/env python

"""This program finish a Design Mode:Observer Mode
"""

class Subject():
    """ a subject object,this is a interface
    """
    def RegisterObserver(self):
        pass

    def RemoveObserver(self):
        pass

    def NotifyObserver(self):
        pass

class Observer():
    """ a observer class,this is a interface,
        all subclass need to finish Updata function
    """
    def Updata(temp,humitidy,press):
        pass

class DisplayElement():
    """ a displayelment class,this is a interface,
        all subclass need to finish display function
    """
    def Display():
        pass


class WeatherData(Subject):
    def __init__(self):
        self.obs_list = []
        self.temperature = 0.0
        self.humitidy = 0.0
        self.pressure = 0.0

    def RegisterObserver(self,obj):
        print "Register one Obeserver"
        self.obs_list.append(obj)
        print len(self.obs_list)

    def RemoveObserver(self,obj):
        del obs_list.delete[obj]

    def NotifyObserver(self):
        for i in self.obs_list:
            i.Updata(self.temperature,self.humitidy,self.pressure)
    
    def MeasureChanged(self):
        self.NotifyObserver()

    def SetMeasurements(self,temperature,humitidy,pressure):
        self.temperature = temperature
        self.humitidy = humitidy
        self.pressure = pressure
        self.MeasureChanged()

class CurrentCondictionDisplay(Observer,DisplayElement):
    def __init__(self,WeatherData):
        self.weatherdata = WeatherData
        self.weatherdata.RegisterObserver(self)
        self.temperature = 0.0
        self.humitidy = 0.0
        self.pressure = 0.0
        
    def Display(self):
        print "Current Condiction: %f F degress and humitidy : %f"\
                ,(self.temperature,self.humitidy)

    def Updata(self,temp,humitidy,pressure):
        self.temperature = temp
        self.humitidy = humitidy
        self.pressure = pressure
        self.Display()

if __name__ == "__main__":
    wd = WeatherData()
    print wd.temperature
    print wd.obs_list
    print wd.pressure
    print wd.humitidy
    cdD = CurrentCondictionDisplay(wd) 

    print "======set some paraments in weather data======"
    wd.SetMeasurements(1.2,3.4,5.6) 
    print cdD.temperature
    print cdD.pressure
    print cdD.humitidy
