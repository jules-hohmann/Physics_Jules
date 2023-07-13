import numpy as np


g = 9.81
# waterdensity
w = 1000


def calculate_buoyancy(p, V):
    if p < 0 or p == 0:
        return ValueError
    if V < 0 or V == 0:
        return ValueError
    buoyancy = p * V * g
    return buoyancy


def will_it_float(V, m):
    if V < 0 or V == 0:
        return ValueError
    if m < 0 or m == 0:
        return ValueError
    gravitationalforce = m * g
    Totalforce = calculate_buoyancy(w, V) - gravitationalforce
    if Totalforce > 0 or Totalforce == 0:
        return True
    if Totalforce < 0:
        return False


def calculate_pressure(d):
    if d < 0:
        return ValueError
    pressure = w * d * g
    return pressure
