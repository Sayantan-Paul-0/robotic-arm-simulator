# 2-Link Planar Robot Arm Simulator

A simulator for a two-link planar robotic arm. Given a target point, it solves
the inverse kinematics to find the joint angles and animates the arm reaching
the target.

## What it does
- **Forward kinematics** — given joint angles, arm/link lengths, computes the           end-effector position.
- **Inverse kinematics** — given a target (x, y), arm/link lengths, computes the joint   angles to
  reach it, using the law of cosines. Includes a reachability check that returns
  `None` for unreachable targets.
- **Animation** — interpolates the joint angles frame by frame and visualizes the
  arm sweeping to the target with matplotlib.

## How to run

- **CLI** - Type python3 animate_arms.py and the program will run
- **IDE** - Open animate_arms.py in an IDE and click on the run button

## Concepts
- Angle composition along the kinematic chain (link 2's world angle = θ1 + θ2).
- Law of cosines for the inverse problem; the interior triangle angle is the
  supplement of the joint angle (θ2 = 180° − φ).
- A forward/inverse round-trip test to verify the two are true inverses.

## Known limitations
- Kinematic only — no physics or joint torque yet (PID control is the next step).
- Returns a single elbow-down solution (elbow-up not yet exposed).
- The origin (d = 0) is treated as unreachable.

## Tech
Python, NumPy, Matplotlib