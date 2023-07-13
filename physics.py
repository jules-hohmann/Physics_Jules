import numpy as np

# gravitaional force
g = 9.81
# waterdensity
w = 1000


# calculates buoyancy based of density of fluid and Volume of object


def calculate_buoyancy(p, V):
    if p <= 0 or V <= 0:
        return ValueError
    buoyancy = p * V * g
    return buoyancy


# uses Volume of object and mass to see if the object will float in water or not
def will_it_float(V, m):
    if V <= 0 or m <= 0:
        return ValueError
    gravitationalforce = m * g
    Totalforce = calculate_buoyancy(w, V) - gravitationalforce
    if Totalforce >= 0:
        return True
    if Totalforce < 0:
        return False


# uses depth to find pressure in water
def calculate_pressure(d):
    if d < 0:
        return ValueError
    pressure = w * d * g
    return pressure
