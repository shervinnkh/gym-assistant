from src.utils import getAngle , getMSError 


#Make rules
def rule_angle_range(kp, p1, p2, p3, minA, maxA):
    angle = getAngle([
        (kp[p1][0], kp[p1][1]),
        (kp[p2][0], kp[p2][1]),
        (kp[p3][0], kp[p3][1])
    ])
    return minA < angle < maxA

def rule_x_distance(kp, p1, p2, threshold):
    diff = getMSError([kp[p1][0] , kp[p2][0]])
    print(kp[p1][0],kp[p2][0])
    print(diff)
    return diff < threshold

def rule_y_distance(kp, p1, p2, threshold):
    diff = getMSError([kp[p1][1] , kp[p2][1]])
    print(kp[p1][1],kp[p2][1])
    print(diff)
    return diff < threshold


def make_angle_rule(i1, i2, i3, minA, maxA):
    return lambda kp, conf, ex: rule_angle_range(kp, ex.checks[i1], ex.checks[i2], ex.checks[i3], minA, maxA)

def make_x_rule(i1, i2, dist):
    return lambda kp, conf, ex: rule_x_distance(kp, ex.checks[i1], ex.checks[i2], dist)
