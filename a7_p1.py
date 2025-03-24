import numpy as np
import matplotlib.pyplot as plt

# Constants
n = 200
a = -1
b = 1
dx = (b - a) / n
T = 0.5

# Define x
x = np.linspace(a, b, n + 1)

# Spectral radius function
def spectral_rad(t, u, rho):
    max_val = -1
    for i in range(n + 1):
        max_val = max(abs(u[i,t]), max_val)
    return max_val

# Initialize arrays for u and h
u = np.zeros((n + 1, 1001))
rho = np.ones((n + 1, 1001))

# Set initial conditions for h(x, 0) and u(x, 0)
for i in range(n + 1):
    if x[i] < 0:
        u[i, 0] = 2
    else:
        u[i, 0] = -2

# Time integration
time = [0]
time_val = 0

# Main loop for time-stepping
for t in range(1001):
    dt = (0.9 * dx) / spectral_rad(t, u, rho)
    time_val += dt
    
    if time_val > T:
        break
    
    time.append(time[-1] + dt)

    for i in range(n + 1):
        l = i - 1
        r = i + 1
        if l == -1:
            l = 0
        if r == n + 1:
            r = n

        # Update rho and u for the next time step
        rho[i, t + 1] = (rho[r, t] + rho[l, t]) / 2 - dt * (rho[r, t] * u[r, t] - rho[l, t] * u[l, t]) / (2 * dx)
        u[i, t + 1] = (rho[r, t] * u[r, t] + rho[l, t] * u[l, t]) / (2 * rho[i, t + 1]) - dt * (rho[r, t] * u[r, t]**2 - (rho[l, t] * u[l, t]**2)) / (2 * dx * rho[i, t + 1])

# Plot the last time step (t = m)
plt.figure(figsize=(12, 6))

# Plot u(x, t) at the final time step
plt.subplot(1, 2, 1)
plt.plot(x, u[:, len(time)-1], label="u(x, t)", color='blue')
plt.title("Velocity at final time step")
plt.xlabel("x")
plt.ylabel("u(x, t)")

# Plot rho(x, t) at the final time step
plt.subplot(1, 2, 2)
plt.plot(x, rho[:, len(time)-1], label="rho(x, t)", color='orange')
plt.title("Density at final time step")
plt.xlabel("x")
plt.ylabel("rho(x, t)")

# Show the plots
plt.tight_layout()
plt.show()

# Print final time
print("Final time:", time_val)
