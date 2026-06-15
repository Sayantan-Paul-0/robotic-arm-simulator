import math
import fk_pos

def ik_pos(L1,L2,x,y):
    """
    Returns the angle of the 2D planar arm
    (theta1,theta2) in degrees,none when target is unreachable
    theta1: angle measure from x axis to link1
    theta2: angle measured from link 2 with respect to link 1
    x,y : position of target point
    """
    #distance from target point to base
    d = math.sqrt(x**2 + y**2)
    cos_phi = (L1**2 + L2**2 - d**2)/ (2*L1*L2)
    if d == 0 or cos_phi < -1 or cos_phi > 1:
        return None
    phi = math.acos(cos_phi)
    theta2 = math.degrees(math.pi - phi)
    theta_target = math.atan2(y,x)
    cos_beta = (L1**2 + d**2 - L2**2) / (2*L1*d)
    #redundant check for cos_beta. cos_phi is the load bearing 
    if cos_beta < -1 or cos_beta > 1:
        return None
    beta = math.acos(cos_beta)
    theta1 = math.degrees(theta_target - beta)
    return theta1,theta2

angles = ik_pos(1,1,1,1)
print('IK Angles:',angles)
print('FK Position:',fk_pos.fk_position(1,1,angles[0],angles[1]))