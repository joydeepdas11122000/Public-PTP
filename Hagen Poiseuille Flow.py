import numpy as np
import scipy.optimize as spo

# Given Data
m = 0.8927 * 0.000001  # kinematic Viscosity (m^2/s)
L = 100  # Length of the Pipe (meter)
R = 0.0254  # Radius of the Pipe (meter)
Q = 0.1  # Flow rate (m^3/s)
e = 0.00015  # Pipe Roughness(m)

u_av = 2  # Average Velocity (m/s)
# u_av = Q / (np.pi * np.power(R, 2))  # Average Velocity (m/s)

R_ed = int((u_av * (2 * R)) / m)  # Reynold's No.
n = e / (2 * R)  # Relative Pipe Roughness


def f(x):
    return (1 / np.power(x, 0.5)) + 2 * np.log10((n / 3.7) + (2.51 / (R_ed * np.power(x, 0.5))))


if R_ed < 2000:
    f_d = 64 / R_ed
else:
    f_d = spo.fsolve(f, 0.01)[0]

h_f = f_d * (L / (2 * R)) * (np.power(u_av, 2) / (2 * 9.81))

print(f"Head loss = {h_f:.3f} m"
      f" \nf_d = {f_d:.3f} (Darcy Friction Factor)"
      f"\nR_ed = {R_ed} (Reynold's No.)"
      f"\nU_av = {u_av:.3f} m/s (Average Velocity)"
      f"\nU_max   = {2*u_av:.3f} m/s (Maximum Velocity)"
      f"\nn = {n:.6f} (Relative Pipe Roughness)")


