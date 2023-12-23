class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True
    
    def turnOff(self):
        self.swithIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness =+ 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness =- 1

            