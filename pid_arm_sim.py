import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from ik_pos import ik_pos
from fk_pos import fk_position

def simulate_pid_arm(L1, L2, target_x, target_y, Kp, Kd, Ki, I, dt=0.01, steps=2000):
    angles = ik_pos(L1, L2, target_x, target_y)
    if angles is None:
        print("Target unreachable"); return None
    theta1_target, theta2_target = angles   # where each joint must end up

    # state: each joint has an angle and an angular velocity
    theta1, theta2 = 0.0, 0.0
    omega1, omega2 = 0.0, 0.0
    integral1,integral2 = 0.0, 0.0
    history = []

    for _ in range(steps):
        error1 = theta1_target - theta1
        integral1 += error1 * dt
        tau1   = (Kp*error1 - Kd*omega1 + Ki*integral1)
        alpha1 = tau1 / I
        omega1 += alpha1 * dt     
        theta1 += omega1 * dt

        error2 = theta2_target - theta2
        integral2 += error2 * dt
        tau2   = (Kp*error2 - Kd*omega2 + Ki*integral2)
        alpha2 = tau2 / I
        omega2 += alpha2 * dt     
        theta2 += omega2 * dt
        history.append((theta1, theta2))
    return history

if __name__ == "__main__":  
    history = simulate_pid_arm(L1=2.0, L2=1.0, target_x=2.0, target_y=2.0, Kp=10, Kd=7, Ki=0.001, I=1.0)
    print("Final angles:", history[-1])
    print("round test:", ik_pos(L1=2.0,L2=1.0,x=2.0,y=2.0))