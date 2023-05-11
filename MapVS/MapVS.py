import ClassDraw
import Logic
import time

NUMOFTESTS = 666
def main():
    wyniki = [0 for x in range(6)]
    drawer = ClassDraw.Draw()
    drawer.clock.tick()
    for x in range(NUMOFTESTS):
        Map = Logic.map()
        run = True

        while run:
            for event in ClassDraw.pygame.event.get():
                if event.type == ClassDraw.pygame.QUIT:
                    run = False
                    ClassDraw.pygame.quit()
            if run:
                for gracz in Map.Players:
                    if gracz.WON == False:
                        drawer.clock.tick(drawer.FPS)
                        new= gracz.Play()
                        if new != -1:
                            Map.SetPawnOnField(gracz.PlayerNumber ,new[0], new[1])
                            drawer.DrawMainMap(Map)
                        if gracz.WON == True:
                            drawer.DrawMainMap(Map)
                            drawer.DrawWonPlayer(gracz.PlayerNumber)
                            wyniki[gracz.PlayerNumber]+= 1
                            time.sleep(3)
                            run = False
                    else:
                        drawer.DrawMainMap(Map)
                        drawer.DrawWonPlayer(gracz.PlayerNumber)
                        wyniki[gracz.PlayerNumber]+= 1
                        time.sleep(3)

                        run = False
    print(wyniki)          
if __name__ == "__main__":
    main()
