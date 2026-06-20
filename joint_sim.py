import numpy as np
import matplotlib.pyplot as plt

def simulate_joint(Kp, Kd, Ki, target, theta_start=0.0, dt=0.01, steps=1000, I=1.0):
    theta = theta_start
    omega = 0.0
    history = []
    integral = 0.0
    for _ in range(steps):
        error = target - theta
        integral += error * dt
        tau   = Kp * error - Kd * omega + Ki * integral      # (P-control)
        alpha = tau / I
        omega = omega + alpha * dt
        theta = theta + omega * dt
        history.append(theta)
    return history

if __name__ == "__main__":
    history = simulate_joint(Kp=10, Kd=6, Ki=0.0001, target=90)    #drive joint from 0 -> 90
    plt.plot(history)
    plt.axhline(90, color='r', linestyle='--', label='target')
    plt.xlabel('timestep'); plt.ylabel('angle'); plt.legend(); plt.show()