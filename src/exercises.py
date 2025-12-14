from src.rules import make_angle_rule , make_x_rule
from src.draw import DrawAction,DrawAngle


class Exercise:
    def __init__(self, id, name, leftChecks , rightChecks , twoSide, rules=None, draws=None):
        
        self.name = name
        self.id = id
        self.leftChecks = leftChecks
        self.rightChecks = rightChecks
        self.twoSide = twoSide
        self.checks = rightChecks
        self.rules = rules if rules else []
        self.draws = draws if draws else []

    def defineRightLeft(self,isRight):
        self.checks = self.rightChecks if isRight else self.leftChecks

    def check(self, kp, conf):
        for rule in self.rules:
            if not rule(kp, conf,self):
                return False
        return True
    
    def defineDrawChecks(self,checks):
        for ins in range(0,len(self.draws)):
            self.draws[ins].p1 = checks[self.draws[ins].ind1]
            self.draws[ins].p2 = checks[self.draws[ins].ind2]
            self.draws[ins].p3 = checks[self.draws[ins].ind3]

    def draw_all_actions(self, image,isCor, kp):
        print("hi")
        print(isCor)
        for i, action in enumerate(self.draws):
            image = action.draw(image, self.draws[i].colorT if isCor else self.draws[i].colorF , kp)
        return image
 

# All exercises
exercises = [
    Exercise(id=0,name='جلو بازو' ,leftChecks=[  11 , 9 , 7 , 5],rightChecks=[12, 10, 8, 6 ],twoSide=False , 
               rules=[
                   make_angle_rule(3, 2, 1, 30, 170),  
                    make_x_rule(3, 2, 0.015),
               ],
               draws=[
                   DrawAngle(3,2,0, colorT=(255, 40, 40), colorF=(255, 40, 40), show_angle=False),
                   DrawAngle(3,2,1, colorT=(60, 179, 113), colorF=(10, 10, 225), show_angle=True)
               ]),
    
    Exercise(id=1,name='سر شونه هالتر' ,leftChecks=[  9 , 7 , 5],rightChecks=[ 10, 8, 6 ],twoSide=True,
               rules=[
                   make_angle_rule(2,1,0,65,280),
               ],
               draws=[
                   DrawAngle(2,1,0, colorT=(60, 179, 113), colorF=(10, 10, 225), show_angle=True)
               ]
               ),
    
    Exercise(id=1,name='لانج' ,leftChecks=[  15,13,11],rightChecks=[ 16,14,12 ],twoSide=False,
               rules=[
                   make_angle_rule(2,1,0,55,190),
               ],
               draws=[
                   DrawAngle(2,1,0, colorT=(60, 179, 113), colorF=(10, 10, 225), show_angle=True)
               ]
               ),

]