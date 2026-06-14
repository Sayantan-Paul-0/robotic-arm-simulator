import math

def fk_position(L1,L2,theta1,theta2):
    """
    Returns the position of the 2D planar arm's 
    end effector (x,y)
    theta1:shoulder angle from x axis
    theta2:elbow angle measured relative to link 1
    theta1 and theta2 are in degrees
    """
    theta1_rad = math.radians(theta1)
    theta2_rad = math.radians(theta2)
    x = L1*math.cos(theta1_rad) + L2*math.cos(theta1_rad+theta2_rad)
    y = L1*math.sin(theta1_rad) + L2*math.sin(theta1_rad+theta2_rad)
    return x,y

def check(result, expected, label):
    ok = math.isclose(result[0], expected[0], abs_tol=1e-9) and \
         math.isclose(result[1], expected[1], abs_tol=1e-9)
    print(f"{'PASS' if ok else 'FAIL'}  {label}: got {result}, expected {expected}")

if __name__ == "__main__":
    check(fk_position(1, 1, 0, 0),    (2, 0), "straight along x")
    check(fk_position(1, 1, 90, 0),   (0, 2), "straight up")
    check(fk_position(1, 1, 0, 90),   (1, 1), "L1 along x, L2 up")
    check(fk_position(1, 1, 90, -90), (1, 1), "L1 up, L2 along x")