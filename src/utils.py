from typing import List,Tuple
import math


def getMSError(values: List[float]) -> float:
    n = len(values)
    if n == 0:
        return 0.0
    
    mean = sum(values) / n
    variance = sum((x - mean)**2 for x in values) / n
    std_dev = math.sqrt(variance)
    return std_dev

def getAngle(points: List[Tuple[float, float]]) -> float:
    if len(points) != 3:
        raise ValueError("فقط باید سه نقطه بدهید")
    
    (x1, y1), (x2, y2), (x3, y3) = points
    
    v1 = (x1 - x2, y1 - y2) 
    v2 = (x3 - x2, y3 - y2) 
    
    dot = v1[0]*v2[0] + v1[1]*v2[1]
    norm1 = math.sqrt(v1[0]**2 + v1[1]**2)
    norm2 = math.sqrt(v2[0]**2 + v2[1]**2)
    
    if norm1 == 0 or norm2 == 0:
        return 0.0
    
    cos_theta = dot / (norm1 * norm2)
    cos_theta = max(min(cos_theta, 1.0), -1.0)
    theta = math.acos(cos_theta)
    
    return math.degrees(theta)




def getRotation(confs):

    rightChecks = [2 , 4, 6, 8 ,10,12 , 14 , 16]
    leftChecks = [1,3,5,7,9,11,13,15]
    isRight = False

    rightMean=0
    leftMean=0

    for rc in rightChecks:
        rightMean+=confs[rc]

    for lc in leftChecks:
        leftMean+=confs[lc]

    rightMean /= len(rightChecks)
    leftMean /= len(leftChecks)

    isRight = rightMean>leftMean
    detected = max(rightMean,leftMean) > 0.7
    print(isRight,detected)
    return isRight,detected
