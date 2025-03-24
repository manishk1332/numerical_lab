import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81
n = 500
a = 0
b = 1
dx = (b - a) / n
T = 0.05

# Define x
x = np.linspace(a, b, n + 1)

# Spectral radius function
def spectral_rad(t, u, h):
    max_val = -1
    for i in range(n + 1):
        lb1 = np.abs(u[i, t] + np.sqrt(g * h[i, t]))
        lb2 = np.abs(u[i, t] - np.sqrt(g * h[i, t]))
        temp_max = max(lb1, lb2)
        max_val = max(temp_max, max_val)
    return max_val

# Initialize arrays for u and h
u = np.zeros((n + 1, 1001))
h = np.ones((n + 1, 1001))

# Set initial conditions for h(x, 0) and u(x, 0)
for i in range(n + 1):
    if x[i] < 0.5:
        u[i, 0] = -5
    else:
        u[i, 0] = 5

# Time integration
time = [0]
time_val = 0

# Main loop for time-stepping
for t in range(1001):
    dt = (0.9 * dx) / spectral_rad(t, u, h)
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

        # Update h and u for the next time step
        h[i, t + 1] = (h[r, t] + h[l, t]) / 2 - dt * (h[r, t] * u[r, t] - h[l, t] * u[l, t]) / (2 * dx)
        u[i, t + 1] = (h[r, t] * u[r, t] + h[l, t] * u[l, t]) / (2 * h[i, t + 1]) - \
                      dt * (h[r, t] * u[r, t]**2 + 0.5 * g * h[r, t]**2 - 
                             (h[l, t] * u[l, t]**2 + 0.5 * g * h[l, t]**2)) / (2 * dx * h[i, t + 1])

# Plot the last time step (t = m)
plt.figure(figsize=(12, 6))

# Plot u(x, t) at the final time step
plt.subplot(1, 2, 1)
plt.plot(x, u[:, len(time)-1], label="u(x, t)", color='blue')
plt.title("Velocity at final time step")
plt.xlabel("x")
plt.ylabel("u(x, t)")

# Plot h(x, t) at the final time step
plt.subplot(1, 2, 2)
plt.plot(x, h[:, len(time)-1], label="h(x, t)", color='orange')
plt.title("Height at final time step")
plt.xlabel("x")
plt.ylabel("h(x, t)")

# Show the plots
plt.tight_layout()
plt.show()

# Print final time
print("Final time:", time_val)
