import CarFollowing as cf
import simulation
import tkinter as tk

app0 = tk.Tk()
app0.title('my app window')

canvas0 = tk.Canvas(app0, width=1200, height=200)
canvas0.pack()


landWidth = 3.2
disp_laneWidth = landWidth * 10.0

print(disp_laneWidth)
linkLength = 300
disp_linkLength = linkLength * 10.0
Y = 20
print("to create", disp_linkLength)
canvas0.create_polygon(20, 20, 20+disp_linkLength, 20, 20+disp_linkLength+500, Y+disp_laneWidth,20, Y+disp_laneWidth, fill='gray')

carLength = 4.5
carWidth = 2.0

disp_carLength = carLength * 10.0
disp_carWidth = carWidth * 10.0
disp_XCar = 25
disp_YCar = 25

car_Gobj = canvas0.create_polygon(disp_XCar, disp_YCar, disp_XCar+disp_carLength, disp_YCar, disp_XCar+disp_carLength, disp_YCar+disp_carWidth, disp_XCar, disp_YCar+disp_carWidth, fill='red', tags="RU_GUI")



stepSize = 0.2
car01 = cf.Car(stepSize)

car02 = cf.Car(stepSize)

time02_L = []
space02_L = []
velocity02_L = []
time03_L = []
space03_L = []
velocity03_L = []

simulationTime = 200
for step in range(0, int(200*stepSize)):
    car02.update()
    print(car02.pos_meter, car02.speed_kmPerHr)

    time02_L.append(stepSize*step)
    space02_L.append(car02.pos_meter)
    velocity02_L.append(car02.speed_meterPerSec)

    if step == 4:
        car03 = cf.Car(stepSize)
        car03.leader = car02
        car03.bigV_meterPerSec = 35
    elif step > 4:
        car03.update()
        # print("         {:.2f}, {:.2f}".format(car03.pos_meter, car03.speed_kmPerHr))
        # print("           dist diff:{:.2f}".format(car02.pos_meter - car03.pos_meter))

        time03_L.append(stepSize*step)
        space03_L.append(car03.pos_meter)
        velocity03_L.append(car03.speed_meterPerSec)

    car01.update()


car_moving_speed = velocity02_L






def moveCar():
    
    canvas0.move(car_Gobj, 1, 0)
    canvas0.after(20, moveCar)

bu1 = tk.Button(app0, text='click to simulate', command=moveCar)
bu1.pack()

app0.mainloop()