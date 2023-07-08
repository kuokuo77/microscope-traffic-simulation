import CarFollowing

class Sim():
    def __init__(self):
        self.endStep = 100
        self.stepSize_sec = 0.5

        assert self.endStep*self.stepSize_sec < 7200

    def run(self):
        step = 0
        endStep = self.endStep
        self.initialization()

        while step < endStep:
            print("-------STEP-------", step)

            self.updateRU(step)
            self.updateInfra()
            self.displayRU()
            self.displayInfra()

            step = step + 1

        self.postDataTreatment()

    def initialization(self):
        self.Car_L = []
        car1 = CarFollowing.Car(self.stepSize_sec)
        self.Car_L.append(car1)

    def updateRU(self, step):
        for carz in self.Car_L:
            carz.update()

        if step == 10:
            car2 = CarFollowing.Car(self.stepSize_sec)
            car2.leader = self.Car_L[0]
            car2.bigV_meterPerSec = 37
            self.Car_L.append(car2)

    def updateInfra(self):
        print("update infrastructure")
    def displayRU(self):
        print("display road user")
    def displayInfra(self):
        print("display infra")
    def postDataTreatment(self):
        print("do some post treatment here")

if __name__ == "__main__":
    sim0 = Sim()
    sim0.run()