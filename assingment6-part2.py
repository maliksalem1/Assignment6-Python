#!/usr/bin//env python3

# Created by: maliksalem1
# Created on: October 2022
# This program compares two numbers


import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

def main():
    while True:
        try:
            radius = float(input("Enter the radius of the sphere: "))
            if radius <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Radius must be a positive number.")
    volume = sphere_volume(radius)
    print("The volume of the sphere is:", volume)

if __name__ == "__main__":
    main()