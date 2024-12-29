#!/usr/bin/env python3
import math
from turtle import *
import turtle


def setupGraph():
    turtle.speed(0)
    turtle.delay(0)
    turtle.hideturtle()
    turtle.update()
    sc = turtle.Screen()
    sc.mode("world")
    turtle.setworldcoordinates(-0.5, -3, max(ddata) + 10, max(hdata) + 10)
    # DRAW THE MOTION GRAPH AXES
    # set origin
    turtle.color("black")
    turtle.home()
    # x-axis
    turtle.forward(max(ddata) + 10)
    turtle.backward(max(ddata) + 20)
    turtle.home()
    # turn and draw y-axis
    turtle.left(90)
    turtle.backward(10)
    turtle.forward(max(hdata) + 20)
    turtle.home()


def drawPoint(coordinate):
    penup()
    goto(coordinate[0], coordinate[1])
    pendown()
    dot(5, "red")
    penup()


def closest_to_zero(nums):
    li = []
    for num in nums:
        li.append(abs(num))
    for num in nums:
        if abs(num) == min(li):
            return num


def printMethod(h, g, m, k, vi, angle, dt, endtime, time, dist):
    # calculate initial x and y velocity
    vy = math.sin(math.radians(angle)) * vi
    vx = math.cos(math.radians(angle)) * vi
    hdata = []
    ddata = []
    timelist = []
    ay = g - k * vx / m
    ax = -k * vx / m
    while time <= endtime:
        print(
            f"Time (s): {time}; Y-Acceleration (m/s^2): {ay}; Y-Velocity (m/s): {vy}; Height (m): {h}; X-Acceleration (m/s^2): {ax}; X-Velocity (m/s): {vx}; Range (m): {dist}"
        )
        hdata.append(h)
        ddata.append(dist)
        timelist.append(time)
        # Y-Components: Accel (gravity), Height, Velocity
        ay = g - k * vy / m
        h = h + dt * (vy)
        vy = vy + dt * (ay)
        # X-Components: Accel, Height, Velocity
        ax = -k * vx / m
        dist = dist + dt * (vx)
        vx = vx + dt * (ax)
        # Plus Delta Time
        time += dt
        time = round(float(time), 3)

    print("-------------GRAPH-SUMMARY----------------")
    minheight = closest_to_zero(hdata)
    indexforminheight = hdata.index(minheight)
    print(f"Max Height: {max(hdata)}")
    print(f"The range and time at the height value closest to 0 at the given dt")
    print(
        f"Height: {minheight}; Time: {timelist[indexforminheight]}; Range: {ddata[indexforminheight]}"
    )


def createGraph(h, g, m, k, vi, angle, dt, endtime, time, dist):
    print("The Graph Window will exit on-click.")
    # calculate initial x and y velocity
    vy = math.sin(math.radians(angle)) * vi
    vx = math.cos(math.radians(angle)) * vi
    global hdata
    global ddata
    hdata = []
    timelist = []
    ddata = []
    ay = g - k * vx / m
    ax = -k * vx / m
    while time <= endtime:
        hdata.append(h)
        ddata.append(dist)
        timelist.append(time)
        # Y-Components: Accel (gravity), Height, Velocity
        ay = g - k * vy / m
        h = h + dt * (vy)
        vy = vy + dt * (ay)
        # X-Components: Accel, Height, Velocity
        ax = -k * vx / m
        dist = dist + dt * (vx)
        vx = vx + dt * (ax)
        # Plus Delta Time
        time += dt
        time = round(float(time), 3)
    print("Range (m) is the x-axis. Height (m) is the y-axis.")
    setupGraph()
    print("-------------GRAPH-SUMMARY----------------")
    minheight = closest_to_zero(hdata)
    indexforminheight = hdata.index(minheight)
    print(f"Max Height: {max(hdata)}")
    print(f"The range and time at the height value closest to 0 at the given dt")
    print(
        f"Height: {minheight}; Time: {timelist[indexforminheight]}; Range: {ddata[indexforminheight]}"
    )
    for h, dist, time in zip(hdata, ddata, timelist):
        drawPoint([dist, h])
    turtle.exitonclick()


def euler():
    h = float(input("Initial height (m): "))
    g = float(input("Absolute Value of Gravity (m/s^2): ")) * (-1)
    m = float(input("Mass (kg): "))
    k = float(input("Drag Coefficient: "))
    vi = float(input("Initial velocity (m/s): "))
    angle = float(input("Launch Angle (degrees): "))
    dt = float(input("Delta Time (s); if 1 then write 1.0: "))
    endtime = float(input("Endtime (s): "))
    graph = input(
        "Would you like a graph? If not, then you will receive standard output (Y/n): "
    )
    time = 0
    dist = 0
    if graph == "Y" or graph == "y":
        createGraph(h, g, m, k, vi, angle, dt, endtime, time, dist)
    elif graph == "N" or graph == "n":
        printMethod(h, g, m, k, vi, angle, dt, endtime, time, dist)
    else:
        print("Rerun program and make (Y/n) = Y, y, N, or n")


def main():
    euler()


if __name__ == "__main__":
    main()
