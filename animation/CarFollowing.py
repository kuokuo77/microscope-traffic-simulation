import math
import matplotlib.pyplot as plt

class RoadUser():
    def update(self):
        raise NotImplementedError('the update method nust be implemented')

class Car(RoadUser):
    def __init__(self, stepSize):
        Car.stepSize = stepSize
        self._pos_meter = 0
        self._speed_meterPerSec = 0

        self.tau = 1.0
        self.bigV_meterPerSec = 30
        self.a_meterPerSecSec = 3.0
        self.length = 5.0

        self.leader = None

        print("a car is instantiated")

    def update(self):
        s1 = self.speedSupposingFreeFlow()
        s2 = self.speedDueToLeader()

        self._speed_meterPerSec = min(s1, s2)
        self._pos_meter = self._pos_meter + self._speed_meterPerSec*self.stepSize

        # print("s1:{:.2f}, s2:{:.2f}, speed(m/s):{:.2f}, position(m):{:.2f}".format(s1, s2, self._speed_meterPerSec, self._pos_meter))

    def speedSupposingFreeFlow(self):
        v = self._speed_meterPerSec
        tau = self.tau
        bigV = self.bigV_meterPerSec
        a = self.a_meterPerSecSec

        return v + 2.5*a*tau*(1 - v/bigV)*math.sqrt(0.025 + v/bigV)
    
    def speedDueToLeader(self):
        if self.leader is None:
            return 999.0
        else:
            xSelf = self._pos_meter
            v = self._speed_meterPerSec

            xLeader = self.leader.pos_meter
            vLeader = self.leader.speed_meterPerSec
            lengthLeader = self.leader.length
            bEstLeader = -4.0
            b = -3.7
            tau = self.tau
            
            return b*tau+math.sqrt(b*b*tau*tau - b*(2*(xLeader-lengthLeader-xSelf) - v*tau - vLeader*vLeader/bEstLeader))
        
    def speedDueToSignal(self):
        
        pass
    
    @property
    def pos_meter(self):
        return self._pos_meter
    @property
    def speed_kmPerHr(self):
        return (3600.0/1000.0)*self._speed_meterPerSec
    @property
    def speed_meterPerSec(self):
        return self._speed_meterPerSec




if __name__ == "__main__":
    stepSize = 0.2
    car01 = Car(stepSize)

    print("test car 02")
    car02 = Car(stepSize)

    time02_L = []
    space02_L = []
    time03_L = []
    space03_L = []

    simulationTime = 200
    for step in range(0, int(200*stepSize)):
        car02.update()
        print(car02.pos_meter, car02.speed_kmPerHr)

        time02_L.append(stepSize*step)
        space02_L.append(car02.pos_meter)


        if step == 4:
            car03 = Car(stepSize)
            car03.leader = car02
            car03.bigV_meterPerSec = 35
        elif step > 4:
            car03.update()
            print("         {:.2f}, {:.2f}".format(car03.pos_meter, car03.speed_kmPerHr))
            print("           dist diff:{:.2f}".format(car02.pos_meter - car03.pos_meter))

            time03_L.append(stepSize*step)
            space03_L.append(car03.pos_meter)

        car01.update()

    plt.plot(time02_L, space02_L)
    plt.plot(time03_L, space03_L)
    plt.xlabel("time")
    plt.ylabel("space")
    plt.show()


    # print("   speed(km/h):{:.2f}".format(car01.speed_kmPerHr))
    # car01.update()
    # print("   speed(km/h):{:.2f}".format(car01.speed_kmPerHr))
    # car01.update()
    # print("   speed(km/h):{:.2f}".format(car01.speed_kmPerHr))