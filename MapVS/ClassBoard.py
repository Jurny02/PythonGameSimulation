import math

class Board:
    def __init__(self, gab) -> None:
        self.FIELDS_FOR_PLAYER = 10
        self.NUMBER_OF_PLAYERS = 6
        self.GAB = gab
        self.DISC = int(self.GAB/math.sqrt(2))
        self.GameFields = self.GenerateGameFields()
        self.HomeFieldsList = self.GenerateHomeFieldsList()
        self.PlayersFields = self.GeneratePlayersFields()
        

    def GenerateGameFields(self):
        List = []
        XCoordinate, YCoordinate =  6* self.DISC, 9*self.GAB + 4 * self.DISC
        for x in range (3):
            XCoordinate += self.GAB
            List.append([XCoordinate, YCoordinate]) 
        for x in range (4):
            YCoordinate -= self.GAB
            List.append([XCoordinate, YCoordinate]) 
        for x in range (4):   
            XCoordinate += self.DISC
            YCoordinate+= self.DISC
            List.append([XCoordinate, YCoordinate]) 
        for x in range (2):   
            XCoordinate += self.DISC
            YCoordinate-= self.DISC
            List.append([XCoordinate, YCoordinate]) 
        for x in range (4):   
            XCoordinate -= self.DISC
            YCoordinate-= self.DISC
            List.append([XCoordinate, YCoordinate]) 
        for x in range (4):   
            XCoordinate += self.DISC
            YCoordinate-= self.DISC
            List.append([XCoordinate, YCoordinate]) 
        for x in range (2):   
            XCoordinate -= self.DISC
            YCoordinate-= self.DISC
            List.append([XCoordinate, YCoordinate]) 
        for x in range (4):   
            XCoordinate -= self.DISC
            YCoordinate+= self.DISC
            List.append([XCoordinate, YCoordinate]) 
        for x in range (4):   
            YCoordinate -= self.GAB
            List.append([XCoordinate, YCoordinate]) 
        for x in range (2):   
            XCoordinate -= self.GAB
            List.append([XCoordinate, YCoordinate]) 
        for x in range (4):   
            YCoordinate += self.GAB
            List.append([XCoordinate, YCoordinate]) 
        for x in range (4):   
            YCoordinate-= self.DISC
            XCoordinate-= self.DISC
            List.append([XCoordinate, YCoordinate]) 
        for x in range (2):   
            YCoordinate+= self.DISC
            XCoordinate-= self.DISC
            List.append([XCoordinate, YCoordinate]) 
        for x in range (4):   
            YCoordinate+= self.DISC
            XCoordinate+= self.DISC
            List.append([XCoordinate, YCoordinate]) 
        for x in range (4):   
            YCoordinate+= self.DISC
            XCoordinate-= self.DISC
            List.append([XCoordinate, YCoordinate]) 
        for x in range (2):   
            YCoordinate+= self.DISC
            XCoordinate+= self.DISC
            List.append([XCoordinate, YCoordinate]) 
        for x in range (4):   
            YCoordinate-= self.DISC
            XCoordinate+= self.DISC
            List.append([XCoordinate, YCoordinate]) 
        for x in range (3):   
            YCoordinate += self.GAB
            List.append([XCoordinate, YCoordinate]) 
        List.append(List.pop(0))
        Final = []
        for x in range (len(List)-1,-1,-1):
            Final.append(List[x])
        return Final

    def GenerateHomeFieldsList(self):
        List = [[],[],[],[],[],[]]
        temp = self.GameFields[40].copy()
        temp[0]+= self.DISC + self.GAB
        temp[1] -= 3* self.DISC
        for x in range(6):
            List[x] = self.GenerateHomeFields(temp)
            temp[1]+= self.DISC + self.GAB
        return List

    def GenerateHomeFields(self,Point):
        List = [(Point[0],Point[1]),(Point[0]+self.DISC, Point[1]),(Point[0]+self.DISC, Point[1]+ self.DISC),(Point[0], Point[1]+self.DISC)]
        return List

    def GeneratePlayersFields(self):
        PlayersFields  = []
        List1 = []
        List2 = []
        List3 = []
        List4 = []
        List5 = []
        List6 = []
        x,y = self.GameFields[59]
        for _ in range (4):
            y -= self.GAB
            List1.append([x, y])
            
        x,y = self.GameFields[9]
        for _ in range (4):
            y -= self.DISC
            x += self.DISC
            List2.append([x, y])

        x,y = self.GameFields[19]
        for _ in range (4):
            y += self.DISC
            x += self.DISC
            List3.append([x, y])
        
        x,y = self.GameFields[29]
        for _ in range (4):
            y += self.GAB
            List4.append([x, y])
    
        x,y = self.GameFields[39]
        for _ in range (4):
            y += self.DISC
            x -= self.DISC
            List5.append([x, y])

        x,y = self.GameFields[49]
        for _ in range (4):
            y -= self.DISC
            x -= self.DISC
            List6.append([x, y])

        PlayersFields.append(List1)
        PlayersFields.append(List2)
        PlayersFields.append(List3)
        PlayersFields.append(List4)
        PlayersFields.append(List5)
        PlayersFields.append(List6)
        return PlayersFields






