import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

from ik_pos import ik_pos
from fk_pos import fk_position
from pid_arm_sim import simulate_pid_arm

def animate_arm(L1, L2, theta1_start, theta2_start, target_x, target_y):
    angles = ik_pos(L1, L2, target_x, target_y)
    if angles is None:
        print("Target unreachable")
        return
    theta1_end, theta2_end = angles

    fig, ax = plt.subplots()
    reach = L1 + L2
    ax.set_xlim(-reach, reach); ax.set_ylim(-reach, reach)
    ax.set_aspect('equal'); ax.grid(True)
    ax.plot(target_x, target_y, 'rx', markersize=10)   # target marker
    line, = ax.plot([], [], 'o-', linewidth=3)         # the arm

    def update(t):
        # t goes 0 -> 1 across the animation
        theta1 = theta1_start + t * (theta1_end - theta1_start)
        theta2 = theta2_start + t * (theta2_end - theta2_start)
        # YOU fill this in:
        elbow_x,elbow_y = L1*np.cos(np.radians(theta1)),L1*np.sin(np.radians(theta1))
        hand_x,hand_y = fk_position(L1, L2, theta1, theta2)
        line.set_data([0, elbow_x, hand_x], [0, elbow_y, hand_y])
        return line,

    frames = np.linspace(0, 1, 60)
    anim = FuncAnimation(fig, update, frames=frames, interval=30, blit=True)
    plt.show()

def animate_pid_arm(L1,L2,target_x,target_y,Kp,Kd,Ki,I):
    history = simulate_pid_arm(L1, L2, target_x, target_y, Kp, Kd, Ki, I)
    if history is None:
        print("Target is unreachable")
        return

    fig, ax = plt.subplots()
    reach = L1 + L2
    ax.set_xlim(-reach,reach); ax.set_ylim(-reach, reach)
    ax.set_aspect('equal'); ax.grid(True)
    ax.plot(target_x,target_y,'rx',markersize = 11)
    line, = ax.plot([], [], 'o-', linewidth=3)

    def update(t):
        theta1, theta2 = history[t]
        elbow_x,elbow_y = L1*np.cos(np.radians(theta1)),L1*np.sin(np.radians(theta1))
        hand_x,hand_y = fk_position(L1, L2, theta1, theta2)
        line.set_data([0, elbow_x, hand_x], [0, elbow_y, hand_y])
        return line,

    anim = FuncAnimation(fig, update, frames=len(history), interval=10, blit=True)
    plt.show()

if __name__ == "__main__":
    #animate_arm(1, 1, 0, 0, 1.5, 0.5)
    animate_pid_arm(L1=2.0, L2=1.0, target_x=2.0, target_y=2.0, Kp=10, Kd=7, Ki=0.001, I=1.0)
