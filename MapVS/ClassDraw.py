from contextlib import nullcontext
import ClassBoard
import pygame
import time

class Draw:
    def __init__(self) -> None:
        pygame.font.init()
        pygame.display.set_caption("LUDO")
        self.clock = pygame.time.Clock()
        self.GAB = 65
        self.GameBoard = ClassBoard.Board(self.GAB)
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.FPS = 60
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (254,254,154)
        self.GREEN = (0,255,0)
        self.PLAYER_GREEN = (0, 102, 0)
        self.RED = (255,0,0)
        self.PLAYER_RED = (128, 0, 0)
        self.BLUE = (0,0,255)
        self.PLAYER_BLUE = (0, 0, 204)
        self.PURPLE = (128,0,128)
        self.PLAYER_PURPLE = (102, 0, 102)
        self.YELLOW = (255, 255, 140)
        self.PLAYER_YELLOW = (255,255,0)
        self.ORANGE = (255, 160, 0)
        self.PLAYER_ORANGE = (255, 153, 51)


        self.PLAYERS_COLORS= [self.GREEN,self.RED,self.PLAYER_BLUE,self.PLAYER_PURPLE,self.PLAYER_YELLOW,self.PLAYER_ORANGE]
        self.PLAYERS_GAME_COLORS= [self.PLAYER_GREEN,self.PLAYER_RED,self.BLUE,self.PURPLE,self.YELLOW,self.ORANGE]
        self.STAT_FONT = pygame.font.SysFont("comicsans", size=int(self.GameBoard.GAB*2/3))
        self.Text = self.STAT_FONT.render("Ludo Game",1, (0,0,0))
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        
        self.RADIUS = int(self.GAB/3.5)

    def DrawWonPlayer(self, PlayerNumber):
        self.WIN.blit(self.STAT_FONT.render("Player WON",0, (self.BLACK)), (50,50))
        self.WIN.blit(self.STAT_FONT.render("Player WON",1, (self.PLAYERS_COLORS[PlayerNumber])), (50,50))

        pygame.display.update()

    def DrawMainMap(self, Map):
        self.WIN.fill(self.GRAY)
        self.WIN.blit(self.Text, (self.GameBoard.GameFields[14][0]+self.GameBoard.DISC, self.GameBoard.GameFields[14][1]-int(self.GameBoard.DISC/2)-7))
        self.DrawGameFields()
        self.DrawHomeFields()
        self.DrawPlayersFields()
        self.DrawPlayerPawns(Map.Fields)
        self.DrawPlayerPawnsHome(Map.Players)
        self.DrawPlayerPawnsFinished(Map.Players)
        self.DrawEndPawns(Map.Players)
        pygame.display.update()

    def DrawGameFields(self):
        for number, Field in enumerate(self.GameBoard.GameFields) :
            if number % self.GameBoard.FIELDS_FOR_PLAYER == 0:
                self.DrawColorField(number//10,Field)
            else:
                 self.DrawEmptyField( Field)
    def DrawPlayersFields(self):
        for number, player in  enumerate(self.GameBoard.PlayersFields):
            for Field in player :
                self.DrawColorField(number,Field)

    def DrawHomeFields(self):
        for number, HomeFields in  enumerate(self.GameBoard.HomeFieldsList):
            for Field in HomeFields :
                self.DrawColorField(number,Field)
    def DrawPlayerPawns(self, Map):
        for x in range (60):
            if Map[x] != -1:
                Field = self.GameBoard.GameFields[x]
                pygame.draw.circle(self.WIN,center=(Field), color= self.BLACK, radius=self.RADIUS-8)
                pygame.draw.circle(self.WIN,center=(Field), color= self.PLAYERS_COLORS[Map[x]], radius=self.RADIUS-11)

    def DrawPlayerPawnsHome(self, Players):
        for y, player in enumerate (Players) :
            for x in range(player.PawnsInHouse):
                pygame.draw.circle(self.WIN,center=(self.GameBoard.HomeFieldsList[y][x]), color= self.BLACK, radius=self.RADIUS-8)
                pygame.draw.circle(self.WIN,center=(self.GameBoard.HomeFieldsList[y][x]), color= self.PLAYERS_COLORS[player.PlayerNumber], radius=self.RADIUS-11)

    def DrawPlayerPawnsFinished(self, Players):
        for y, player in enumerate (Players) :
            for x in range(player.Finished):
                temp = 3 - x
                pygame.draw.circle(self.WIN,center=(self.GameBoard.PlayersFields[y][temp]), color= self.BLACK, radius=self.RADIUS-8)
                pygame.draw.circle(self.WIN,center=(self.GameBoard.PlayersFields[y][temp]), color= self.PLAYERS_COLORS[player.PlayerNumber], radius=self.RADIUS-11)
    def DrawEndPawns(self, Players):
        for n, player in enumerate(Players):
            for Pawn in player.PawnsPosiotion:
                if Pawn>59:
                    temp = Pawn %60
                    pygame.draw.circle(self.WIN,center=(self.GameBoard.PlayersFields[n][temp]), color= self.BLACK, radius=self.RADIUS)# to change to 8
                    pygame.draw.circle(self.WIN,center=(self.GameBoard.PlayersFields[n][temp]), color= self.PLAYERS_COLORS[player.PlayerNumber], radius=self.RADIUS-11)

    def DrawColorField(self, number, Field):
        pygame.draw.circle(self.WIN,center=(Field), color= self.BLACK, radius=self.RADIUS)
        pygame.draw.circle(self.WIN,center=(Field), color= self.PLAYERS_COLORS[number], radius=self.RADIUS-2)
        pygame.draw.circle(self.WIN,center=(Field), color= self.BLACK, radius=self.RADIUS-5)
        pygame.draw.circle(self.WIN,center=(Field), color= self.WHITE, radius=self.RADIUS-6)

    def DrawEmptyField(self, Field):
        pygame.draw.circle(self.WIN,center=(Field), color= self.BLACK, radius=self.RADIUS)
        pygame.draw.circle(self.WIN,center=(Field), color= self.WHITE, radius=self.RADIUS-2)




