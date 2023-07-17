import numpy as np
import math
import matplotlib.pyplot as plt

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


def calculate_auv_acceleration(
    F_magnitude, F_angle, mass=100, Volume=0.1, thrustdistance=0.5
):
    """takes the magnitude of force and angle of force to find the acceleration, returns a vector"""
    Fx = 2 * np.cos(F_angle) * F_magnitude - 2 * np.sin(F_angle) * F_magnitude
    Fy = 2 * np.sin(F_angle) * F_magnitude - 2 * np.cos(F_angle) * F_magnitude
    ax = Fx / mass
    ay = Fy / mass
    acceleration = [ax, ay]
    return acceleration


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thrusterdistance=0.5
):
    """uses magnitude of force and angle and thrusterdistance to calculate angular acceleration"""
    torque = np.sin(F_angle) * F_magnitude * thrusterdistance
    a = inertia / torque
    return a


def calculate_auv2_acceleration(T, alpha, mass):
    if mass <= 0:
        return ValueError
    if len(T) != 4:
        return ValueError
    M = [
        [np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
        [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)],
    ]
    F = np.dot(M, T)
    a = [F[0] / mass, F[1] / mass]
    return a


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia):
    if len(T) != 4:
        return ValueError
    if inertia <= 0:
        return ValueError
    r = np.sqrt(np.power(L, 2) + np.power(l, 2))
    torques = [0, 0, 0, 0]
    for i in range(4):
        torques[i] = T[i] * np.sin(alpha) * L + T[i] * np.cos(alpha) * l
    a = (torques[0] + torques[1] + torques[2] + torques[3]) / inertia
    return a


def simulate_auv2_motion(
    T, alpha, L, l, mass=100, inertia=100, dt=0.1, t_final=10, x0=0, y0=0, theta0=0
):
    a = calculate_auv2_acceleration(T, alpha, mass)
    t = np.arange(0, t_final, dt)
    ax = np.zeros_like(t)
    ay = np.zeros_like(t)
    vx = np.zeros_like(t)
    vy = np.zeros_like(t)
    x = np.zeros_like(t)
    y = np.zeros_like(t)

    angularA = calculate_auv2_angular_acceleration(T, alpha, L, l, inertia)
    omega = np.zeros_like(t)
    theta = np.zeros_like(t)
    for i in range(1, len(t)):
        ax[i] = a[0]
        vx[i] = ax[i] * t[i]
        x[i] = 0.5 * ax[i] * np.power(t[i], 2) + x0

        ay[i] = a[1]
        vy[i] = ay[i] * t[i]
        y[i] = 0.5 * ay[i] * np.power(t[i], 2) + y0

        omega[i] = angularA * t[i]
        theta[i] = 0.5 * angularA * np.power(t[i], 2)
        pass
    a = np.array([ax, ay])
    v = np.array([vx, vy])
    return (t, x, y, theta, v, omega, a)


def plot_auv2_motion(t, x, y, theta, v, omega, a):
    plt.plot(t, x, label="x")
    plt.plot(t, y, label="y")
    plt.plot(t, v[0], label=" X Velocity")
    plt.plot(t, v[1], label="y velocity")
    plt.plot(t, a[0], label="X Acceleration")
    plt.plot(t, a[1], label="y acceleration")
    plt.xlabel("Time (s)")
    plt.ylabel("x (m), y(m),  Velocity (m/s), Acceleration (m/s^2)")
    plt.legend()
    plt.show()
