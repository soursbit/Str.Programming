import math

x = 0
y = 0


while x <= 2:
    y = 3*math.cos(x)-math.fabs(x - 4) + 2
    print("X = %.1f"% x," Y = %.3f"%y)
    x = x + 0.2
