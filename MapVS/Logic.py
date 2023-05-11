FIELDS_FOR_PLAYER = 10
NUMBER_OF_PLAYERS = 6
import random
class map:
    def __init__(self) -> None:
        self.Players =[Player(x) for x in range(6)] # tworze 6 graczy z numerami od 0 do 5
        self.Fields =[-1 for x in range (FIELDS_FOR_PLAYER*NUMBER_OF_PLAYERS)] # 0 to 59

    def IfFieldOccupied(self,Player,FieldNumber):
        if self.Fields[FieldNumber] != 0:
            return True
        return False

    def SetPawnOnField(self, PlayerNumber ,FieldNumber, OldFieldNumber): #wyrzuca pionki z nowozajetego pola
        if OldFieldNumber > -1: #jak old zwroci -1, to nic nie rob
            self.Fields[OldFieldNumber] = -1
        if FieldNumber > -1: # jesli new pole jest rowne -1, to nic nie rob
            if self.Fields[FieldNumber] != -1:
                gamerNumber = self.Fields[FieldNumber]
                gamer = self.Players[gamerNumber]
                gamer.PawnsPosiotion[gamer.PawnsPosiotion.index((FieldNumber - gamer.PlayerOffset)%60)] = 0 #usun kogos pionka z nowo zajetego pola
            self.Fields[FieldNumber] = PlayerNumber

class Player:
    def __init__(self, Number):
        self.PlayerNumber = Number
        self.PlayerOffset = self.PlayerNumber * FIELDS_FOR_PLAYER
        self.PawnsPosiotion = [-2,-2,-2,-2]
        self.Finished = 0 
        self.MoreThrows = True
        self.WON = False
        self.PawnsInHouse =  0
        self.UpdatePlayer()

    def UpdatePlayer(self):
        self.PawnsInHouse =  self.PawnsPosiotion.count(-2)
        self.Finished =  self.PawnsPosiotion.count(-1)
        self.InGamePawns = 4 - self.PawnsInHouse - self.Finished
        if self.InGamePawns == 0 and self.PawnsInHouse > 0:
            self.MoreThrows = True
        else:
            self.MoreThrows = False
        self.LastPossibleField =  NUMBER_OF_PLAYERS * FIELDS_FOR_PLAYER  + 3 - self.Finished
        if self.Finished == 4:
            self.WON = True

    def Throw(self):
        Steps = []
        if self.MoreThrows == True:
            for _ in range (3):
                Steps.append(random.randint(1,6))
                while Steps[-1] == 6 :
                        Steps.append(random.randint(1,6))
                if Steps.count(6) > 0:
                    return Steps
                Steps = []
            return -1
        else:
            Steps.append(random.randint(1,6))
            while Steps[-1] == 6 :
                Steps.append(random.randint(1,6))
            return Steps

    def Play(self): 
        self.UpdatePlayer() #aktualizuje sytuacje gracza przed swoja tura
        if self.WON == False:
            Steps = self.Throw() #zwraca rzut kostki
            if self.MoreThrows == True: #sprawdza, czy zawodnik ma prawo do wiekszej ilosci rzutow
                if Steps == -1: #jak nie trafi 6, to zwraca -1 i oddaje ture
                    return -1
                return self.PlayNewPawn(Steps) #jak wypadnie chociaz jedna 6, to gdy to mozliwe zagrywa nowego pionka 
            else:
                self.PawnsPosiotion.sort() #sortuje tablice pionkow gracza, aby prosciej ruszac od pionka, ktory jest najdalej
                return self.BigFirst(Steps) # zwraca nowa i stara pozycje pionka
        return -1,-1

    def PlayNewPawn(self, Steps):
        Sum = sum(Steps[1:]) #liczy sume oczek poza pierwsza 6
        Index = self.PawnsPosiotion.index(-2) #zwraca pierwszy index pionka ktory jest w domu
        StartPosition = self.PawnsPosiotion[Index] # -2

        if self.PawnsPosiotion.count(Sum) == 0 and Sum <= self.LastPossibleField: # sprawdza, czy suma oczek miesci sie na mapie i czy koncowe pole jest zajete przez naszego pionka
            self.PawnsPosiotion[Index] = Sum #jesli nie, to przenosimy tam pionka

            if self.PawnsPosiotion[Index] == self.LastPossibleField: #sprawdzamy, czy nowe pole jest polem koncowym
                    self.PawnsPosiotion[Index] = -1 #jak tak, ustawiamy wartosc pola na -1 
                    return -1, self.ConvertToMapField(StartPosition)# zwracamy nowe pole -1 aby nie uruchomic funkcji
        else:
            PossibleStep = self.PossibleSteps(Steps,Index) # sprawdzamy, ile dany pionek moze sie poruszyc
            if PossibleStep > 0 : #jesli moze sie poruszyc
                self.PawnsPosiotion[Index] = PossibleStep #przypisujemy mu nowe pole
                if self.PawnsPosiotion[Index] == self.LastPossibleField:
                    print("kurwa mac")
                    self.PawnsPosiotion[Index] = -1
                    return -1, self.ConvertToMapField(StartPosition)
            else:
                if self.PawnsPosiotion.count(0) == 0: #jak nie moze, sprawdzamy, czy bazowe pole jest zajete przez naszego pionka
                    self.PawnsPosiotion[Index] = 0 #jak nie, to nadajemu mu index pola poczatkowego czyli 0
                else:
                    return -1, self.ConvertToMapField(StartPosition) #gdy nie mozemy sie poruszyc i zajete jest pole, zwracamy nowe pole -1 aby nie uruchomic funkcji SetPawnOnFieldi pole -1 aby nie usuwac zadnego pola
        return self.ConvertToMapField(self.PawnsPosiotion[Index]) , self.ConvertToMapField(StartPosition) # zwraca nowe pole i -1 aby nie usuwac pola

    def PossibleSteps(self, Steps, Index): #przyjmuje rzut kostki i index sprawdzanego pionka
        StepsTotal = 0 #tu przechowuje mozliwe kroki
        for step in Steps: 
            if self.PawnsPosiotion[Index] + step + StepsTotal <= self.LastPossibleField and self.PawnsPosiotion.count(self.PawnsPosiotion[Index] + step + StepsTotal) == 0: #sprawdzam, czy pole jest okupowane i czy sie miesci w przedziale
                StepsTotal += step
            else:
                break
        return StepsTotal
    def BigFirst(self, Steps):
        Sum = sum(Steps)
        for Index in range (3,3-self.InGamePawns ,-1):
            StartPosition = self.PawnsPosiotion[Index]
            
            if self.PawnsPosiotion[Index] + Sum <= self.LastPossibleField and self.PawnsPosiotion.count(self.PawnsPosiotion[Index] + Sum) == 0:
                self.PawnsPosiotion[Index] = self.PawnsPosiotion[Index] + Sum

                if self.PawnsPosiotion[Index] == self.LastPossibleField:
                    self.PawnsPosiotion[Index] = -1
                    return -1, self.ConvertToMapField(StartPosition)

                return self.ConvertToMapField(self.PawnsPosiotion[Index]),  self.ConvertToMapField(StartPosition) #returns field for checking
            else:
                PossibleStep = self.PossibleSteps(Steps,Index)
                if PossibleStep > 0 :
                    self.PawnsPosiotion[Index] = self.PawnsPosiotion[Index] + PossibleStep
                    if self.PawnsPosiotion[Index] == self.LastPossibleField:
                        self.PawnsPosiotion[Index] = -1
                        return -1, self.ConvertToMapField(StartPosition)
                    return self.ConvertToMapField(self.PawnsPosiotion[Index]), self.ConvertToMapField(StartPosition)  #returns field for checking 
        if Steps.count(6) > 0 and self.PawnsInHouse > 0:
            return self.PlayNewPawn(Steps) #jak wypadnie chociaz jedna 6, to gdy to mozliwe zagrywa nowego pionka
        return -1
    
    def showPosition(self):
        for number, pawn in enumerate(self.PawnsPosiotion):
            print("pionek nr", number, "pozycja :", self.ConvertToMapField( pawn ) , "gracz ",self.PlayerNumber)
            #print("pionek nr", number, "pozycja :",  pawn  , "gracz ",self.PlayerNumber)
        print()

    def ConvertToMapField(self, Number):
        if Number == -2 or Number == -1 :
            return Number
        if Number > 59:
            return -1
        return (Number + self.PlayerOffset )%(FIELDS_FOR_PLAYER*NUMBER_OF_PLAYERS)

        

