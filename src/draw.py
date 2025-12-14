from typing import List,Tuple
import math
import cv2

class DrawAction:
    def draw(self, image, kp):
        return image

class DrawAngle(DrawAction):
    def __init__(self,ind1,ind2,ind3,colorT=(0,0,255),colorF=(0,0,255), show_angle=True):
        self.ind1 = ind1
        self.ind2 = ind2
        self.ind3 = ind3

        self.p1 = []
        self.p2 = []
        self.p3 = []

        self.colorT = colorT
        self.colorF = colorF
        self.show_angle = show_angle

    def draw(self, image,color, kp ):
        points = [
            (kp[self.p1][0], kp[self.p1][1]),
            (kp[self.p2][0], kp[self.p2][1]),
            (kp[self.p3][0], kp[self.p3][1])
        ]
        return draw_angle_on_image(
            image,
            points,
            color,
            self.show_angle
        )
    
def draw_angle_on_image(image, points: List[Tuple[float, float]],color = (0,0,0), show_angle: bool = False):
    

    for i in range(len(points) - 1):
        start = (int(points[i][0]), int(points[i][1]))
        end = (int(points[i+1][0]), int(points[i+1][1]))
        cv2.line(image, start, end, color, thickness=3, lineType=cv2.LINE_AA)

    for idx, (x, y) in enumerate(points):
        center = (int(x), int(y))
        cv2.circle(image, center, 7, color, -1, lineType=cv2.LINE_AA)
        cv2.circle(image, center, 10, color, 2, lineType=cv2.LINE_AA)

    if show_angle and len(points) == 3:
        (x1, y1), (x2, y2), (x3, y3) = [(int(p[0]), int(p[1])) for p in points]
        v1 = (x1 - x2, y1 - y2)
        v2 = (x3 - x2, y3 - y2)
        dot = v1[0]*v2[0] + v1[1]*v2[1]
        norm1 = math.sqrt(v1[0]**2 + v1[1]**2)
        norm2 = math.sqrt(v2[0]**2 + v2[1]**2)
        if norm1 == 0 or norm2 == 0:
            angle = 0.0
        else:
            cos_theta = max(min(dot / (norm1 * norm2), 1.0), -1.0)
            angle = math.degrees(math.acos(cos_theta))
        cv2.putText(image, f"{angle:.1f} deg", (x2 + 10, y2 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2, lineType=cv2.LINE_AA)

    return image