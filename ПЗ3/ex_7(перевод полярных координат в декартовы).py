from math import sin, cos

def polar_cord(R,angle):
    x = R*cos(angle)
    y = R*sin(angle)
    return x,y

print(polar_cord(2,45))