# PHOTON ORBIT AROUND A SPHERICALLY SYMMETRIC BODY


import math
import matplotlib.pyplot as pyplot

print("\nEnter M, the mass of the orbited body, in kilograms:")
mass = float(input("(Please use scientific notation, i.e. (1.989)*(10**30) ) "))

phi0 = float(input("\nEnter phi0, the initial angle from the X axis, in radians: "))

r0 = float(input("\nEnter, r0 the photon's distance from the center of the orbited body: "))


h = float(input("\nEnter h, the change in angle for the first calculation: "))


print("\nEnter dr, the change in radius for the first calculation:") 
dr = float(input("(Please enter it as in terms of the Schwarzschild radius, i.e. 0.01, -0.001, or 0) "))


G = (6.674)*(10**(-11))  # Gravitational Constant
c = 299792458  # Speed of light
rS = (2*G*mass)/(c*c)  #Schwarzschild radius


u0 = rS/r0

phi1 = phi0 + h
u1 = rS/(r0+dr)
r1 = r0 + dr

phiList = [phi0, phi1]
uList = [u0, u1]
rList = [r0, r1]

u2=1  # Initialize to a non-negative value to begin the loop
   
while ((phi1 < phi0+(2*math.pi)) and (rS/u2 >= 0)):
    
    u2 = (2+((h**2)*(((3/2)*u1)-1)))*u1-u0
    
    if (rS/u2 >= 0):
        uList.append(u2)

        u0 = u1
        u1 = u2
        phi1 += h 

        phiList.append(phi1)
        rList.append(rS / u2)



pyplot.axes(polar = True)
pyplot.plot(phiList, rList)
pyplot.show()

