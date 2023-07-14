import numpy as np
import math

# gravitaional force
g = 9.81
# waterdensity
w = 1000


def calculate_buoyancy(p, V):
    """calculates buoyancy based of density of fluid and Volume of object"""
    """does not accept a pressure or Volume less than or equal to 0"""
    if p <= 0 or V <= 0:
        return ValueError
    buoyancy = p * V * g
    return buoyancy


def will_it_float(V, m):
    """uses Volume of object and mass to see if the object will float in water or not"""
    """does not accept volume or mass of less than or equal to 0"""
    if V <= 0 or m <= 0:
        return ValueError
    gravitationalforce = m * g
    Totalforce = calculate_buoyancy(w, V) - gravitationalforce
    if Totalforce > 0:
        return True
    if Totalforce < 0:
        return False
    else:
        return None


def calculate_pressure(d):
    """uses depth to find pressure in water"""
    """does not accept a depth of less than 0"""
    if d < 0:
        return ValueError
    pressure = w * d * g
    return pressure


def calculate_acceleration(F, m):
    "" "takes force and mass to calculate the acceleration" ""
    """Function cannot take a mass less than or equal to 0"""
    if m <= 0:
        return ValueError
    a = F / m
    return a


def calculate_angular_acceleration(tau, I):
    """uses the torque and moment of Inirtia to calculate angular acceleration"""
    """Inertia cannot be negative or equal to 0 or the function will return an error"""
    if I <= 0:
        return ValueError
    a = tau / I
    return a


def calculate_moment_of_inertia(m, r):
    """uses the mass and the distance from axis of rotation to calculate Inertia"""
    """neither mass or distance can be negative so the function returns error"""
    if m <= 0 or r < 0:
        return ValueError
    I = m * np.power(r, 2)
    return I


mass = 100
Volume = 0.1
thrusterdistance = 0.5


def calculate_auv_acceleration(F_magnitude, F_angle):
    """takes the magnitude of force and angle of force to find the acceleration, returns a vector"""
    Fx = 2 * np.cos(F_angle) * F_magnitude - 2 * np.sin(F_angle) * F_magnitude
    Fy = 2 * np.sin(F_angle) * F_magnitude - 2 * np.cos(F_angle) * F_magnitude
    ax = Fx / mass
    ay = Fy / mass
    acceleration = np.array[ax, ay]
    return acceleration


inertia = 1


def calculate_auv_angular_acceleration(F_magnitude, F_angle):
    """uses magnitude of force and angle to calculate acceleration"""
    torque = np.sin(F_angle) * F_magnitude * thrusterdistance
    a = inertia / torque
    return a
