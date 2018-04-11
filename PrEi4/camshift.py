## Nouveau code ##
from psonic import *
import cv2
import numpy as np
from threading import Thread
import scipy as sp
from scipy import ndimage

### Capture de la video avec la webcam ###

cap = cv2.VideoCapture(0)
ret, image = cap.read()

### on récupere la première image en niveau de gris ###
previous = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
### on récupere le nombre de points ###
somme_points = previous.shape[0] * previous.shape[1]

### Variable global ###
tx = 0.3
lower_blue = np.array([70, 50, 50])  # teinte basse du bleu
upper_blue = np.array([150, 200, 255])  # teinte haute du bleu

def rectangle(p1,p2,color):
    cv2.rectangle(frame, p1, p2, color, thickness=2, lineType=1)

def text(note,point):
    txt=cv2.putText(frame, note, point, 2, 1 / 2, (0, 0, 0), 2, cv2.LINE_4)
    cv2.flip(txt, 1)
def cercle(centre,rayon,color,thickeness):
    cv2.circle(frame, centre, rayon, color, thickness=thickeness, lineType=2)

def AffichageSpirale():

    cercle((320, 240), 10, (255, 255, 255),-5)
    cercle((320, 240), 110, (255, 0, 0),2)
    cercle((320, 240), 160, (0, 255, 255),2)
    cercle((320, 240), 210, (0, 0, 255),2)

    rectangle((310, 20), (330, 40), (0, 0, 255))
    rectangle((450, 90), (470, 110), (0, 0, 255))
    rectangle((500, 260), (520, 280), (0, 0, 255))
    rectangle((400, 395), (420, 415), (0, 0, 255))
    rectangle((230, 390), (250, 410), (0, 0, 255))
    rectangle((145, 275), (165, 295), (0, 0, 255))
    rectangle((195, 110), (215, 130), (0, 0, 255))
    rectangle((310, 70), (330, 90), (0, 255, 255))
    rectangle((410, 120), (430, 140), (0, 255, 255))
    rectangle((450, 250), (470, 270), (0, 255, 255))
    rectangle((370, 350), (390, 370), (0, 255, 255))
    rectangle((255, 345), (275, 365), (0, 255, 255))
    rectangle((197, 260), (217, 280), (0, 255, 255))
    rectangle((230, 150), (250, 170), (0, 255, 255))
    rectangle((310, 120), (330, 140), (255, 0, 0))

    rectangle((550, 300), (620, 340), (0, 255, 255))

def AffichageDP():

    rectangle((550, 20), (620, 60), (0, 0, 255))
    rectangle((550, 70), (620, 110), (0, 0, 255))
    rectangle((550, 120), (620, 160), (0, 0, 255))
    rectangle((550, 170), (620, 210), (0, 0, 255))



def AffichageNotes():

    text("DO", (310, 15))  # C
    text("SI", (480, 90))  # D
    text("LA", (540, 280))  # E
    text("SOL", (420, 440))  # F
    text("FA", (210, 450))  # G
    text("MI", (95, 310))  # A
    text("RE", (140, 100))  # B


## Pour chaque frame ##

while (1):

    ret, frame = cap.read()  # on récupère la frame


    ## Si le frame est ok ##
    if ret:

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Mask pour récupérer l’image qu’avec les composantes de bleu
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        previous = np.copy(mask)

        # Permet de joindre deux tableaux, et donc de rajouter la couleur sur le mask
        res = cv2.bitwise_and(frame, frame, mask=mask)

        # On cherche à savoir si il y a assez de points bleu
        somme_points_blancs = np.sum(mask)
        taux = float(somme_points_blancs) / float(somme_points)

        if taux > tx:
            x, y = np.where(mask)  ## donne les indices dans le tableau mask du barycentre des points
            x_c, y_c = np.mean(x), np.mean(y)  # donne les coordonnées
            cercle((int(np.round(y_c)), int(np.round(x_c))), 20, (108, 0, 46),-8)

            AffichageSpirale()
            AffichageDP()

            #### SPIRALE NOTES ####

            if (x_c>20 and x_c<40 and y_c>310 and y_c<330):
                run("""
                    play :C3
                    live_loop :foo do
                          use_real_time
                          a, b, c = sync "/osc/trigger/prophet"
                          synth :prophet, note: a, cutoff: b, sustain: c
                end """)

                run("""live_loop :foo do
                          use_real_time
                          a, b, c, d = sync "/osc/trigger/mod_fm"
                          synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                        end """)
            if (x_c > 90 and x_c < 110 and y_c > 450 and y_c < 470 ):
                run("""
                                    play :D3
                                    live_loop :foo do
                                          use_real_time
                                          a, b, c = sync "/osc/trigger/prophet"
                                          synth :prophet, note: a, cutoff: b, sustain: c
                                end """)

                run("""live_loop :foo do
                                          use_real_time
                                          a, b, c, d = sync "/osc/trigger/mod_fm"
                                          synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                        end """)
            if (x_c > 260 and x_c < 280 and y_c > 500 and y_c < 520 ):
                run("""
                                    play :E3
                                    live_loop :foo do
                                          use_real_time
                                          a, b, c = sync "/osc/trigger/prophet"
                                          synth :prophet, note: a, cutoff: b, sustain: c
                                end """)

                run("""live_loop :foo do
                                          use_real_time
                                          a, b, c, d = sync "/osc/trigger/mod_fm"
                                          synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                        end """)
            if (x_c > 395 and x_c < 415 and y_c > 400 and y_c < 420):
                run("""
                                    play :F3
                                    live_loop :foo do
                                          use_real_time
                                          a, b, c = sync "/osc/trigger/prophet"
                                          synth :prophet, note: a, cutoff: b, sustain: c
                                end """)

                run("""live_loop :foo do
                                          use_real_time
                                          a, b, c, d = sync "/osc/trigger/mod_fm"
                                          synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                        end """)
            if (x_c > 390 and x_c < 410 and y_c > 230 and y_c < 250):
                run("""
                                    play :G3
                                    live_loop :foo do
                                          use_real_time
                                          a, b, c = sync "/osc/trigger/prophet"
                                          synth :prophet, note: a, cutoff: b, sustain: c
                                end """)

                run("""live_loop :foo do
                                          use_real_time
                                          a, b, c, d = sync "/osc/trigger/mod_fm"
                                          synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                        end """)
            if (x_c > 275 and x_c < 295 and y_c > 145 and y_c < 165):
                run("""
                                    play :A3
                                    live_loop :foo do
                                          use_real_time
                                          a, b, c = sync "/osc/trigger/prophet"
                                          synth :prophet, note: a, cutoff: b, sustain: c
                                end """)

                run("""live_loop :foo do
                                          use_real_time
                                          a, b, c, d = sync "/osc/trigger/mod_fm"
                                          synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                        end """)
            if (x_c > 110 and x_c < 130 and y_c > 195 and y_c < 215):
                run("""
                                    play :B3
                                    live_loop :foo do
                                          use_real_time
                                          a, b, c = sync "/osc/trigger/prophet"
                                          synth :prophet, note: a, cutoff: b, sustain: c
                                end """)

                run("""live_loop :foo do
                                          use_real_time
                                          a, b, c, d = sync "/osc/trigger/mod_fm"
                                          synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                        end """)
            if (x_c > 70 and x_c < 90 and y_c > 310 and y_c < 330):
                run("""
                                        play :C4
                                        live_loop :foo do
                                              use_real_time
                                              a, b, c = sync "/osc/trigger/prophet"
                                              synth :prophet, note: a, cutoff: b, sustain: c
                                    end """)

                run("""live_loop :foo do
                                              use_real_time
                                              a, b, c, d = sync "/osc/trigger/mod_fm"
                                              synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                            end """)
            if (x_c > 120 and x_c < 140 and y_c > 410 and y_c < 430 ):
                run("""
                                            play :D4
                                            live_loop :foo do
                                                  use_real_time
                                                  a, b, c = sync "/osc/trigger/prophet"
                                                  synth :prophet, note: a, cutoff: b, sustain: c
                                        end """)

                run("""live_loop :foo do
                                                  use_real_time
                                                  a, b, c, d = sync "/osc/trigger/mod_fm"
                                                  synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                                end """)
            if (x_c > 250 and x_c < 270 and y_c > 450 and y_c < 470):
                run("""
                                                play :E4
                                                live_loop :foo do
                                                      use_real_time
                                                      a, b, c = sync "/osc/trigger/prophet"
                                                      synth :prophet, note: a, cutoff: b, sustain: c
                                            end """)

                run("""live_loop :foo do
                                                      use_real_time
                                                      a, b, c, d = sync "/osc/trigger/mod_fm"
                                                      synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                                    end """)
            if (x_c > 350 and x_c < 370 and y_c > 370 and y_c < 390):
                run("""
                                                    play :F4
                                                    live_loop :foo do
                                                          use_real_time
                                                          a, b, c = sync "/osc/trigger/prophet"
                                                          synth :prophet, note: a, cutoff: b, sustain: c
                                                end """)

                run("""live_loop :foo do
                                                          use_real_time
                                                          a, b, c, d = sync "/osc/trigger/mod_fm"
                                                          synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                                    end """)
            if (x_c > 345 and x_c < 365 and y_c > 255 and y_c < 275):
                run("""
                                                        play :G4
                                                        live_loop :foo do
                                                              use_real_time
                                                              a, b, c = sync "/osc/trigger/prophet"
                                                              synth :prophet, note: a, cutoff: b, sustain: c
                                                    end """)

                run("""live_loop :foo do
                                                              use_real_time
                                                              a, b, c, d = sync "/osc/trigger/mod_fm"
                                                              synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                                            end """)
            if (x_c > 260 and x_c < 280 and y_c > 197 and y_c < 217 ):
                run("""
                                                            play :A4
                                                            live_loop :foo do
                                                                  use_real_time
                                                                  a, b, c = sync "/osc/trigger/prophet"
                                                                  synth :prophet, note: a, cutoff: b, sustain: c
                                                        end """)

                run("""live_loop :foo do
                                                                  use_real_time
                                                                  a, b, c, d = sync "/osc/trigger/mod_fm"
                                                                  synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                                                end """)
            if (x_c > 150 and x_c < 170 and y_c > 230 and y_c < 250 ):
                run("""
                                                                play :B4
                                                                live_loop :foo do
                                                                      use_real_time
                                                                      a, b, c = sync "/osc/trigger/prophet"
                                                                      synth :prophet, note: a, cutoff: b, sustain: c
                                                            end """)

                run("""live_loop :foo do
                                                                      use_real_time
                                                                      a, b, c, d = sync "/osc/trigger/mod_fm"
                                                                      synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                                                    end """)
            if (x_c > 120 and x_c < 140 and y_c > 310 and y_c < 330):
                run("""
                                                                play :C5
                                                                live_loop :foo do
                                                                      use_real_time
                                                                      a, b, c = sync "/osc/trigger/prophet"
                                                                      synth :prophet, note: a, cutoff: b, sustain: c
                                                            end """)

                run("""live_loop :foo do
                                                                      use_real_time
                                                                      a, b, c, d = sync "/osc/trigger/mod_fm"
                                                                      synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                                                    end """)


            #### DAFT PUNK ####

            if (x_c > 20 and x_c < 60 and y_c > 550 and y_c < 620 and one1==True):
                run("""
                        use_bpm 123

                        sample "C:/Users/Nathan/Documents/GitHub/Projet-Musique/Projet-Musique/PrEi4/samples/Harder.wav"

                        """)

                run("""live_loop :foo do
                                                              use_real_time
                                                              a, b, c, d = sync "/osc/trigger/mod_fm"
                                                              synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                                            end """)
                one1 = False
            if (x_c > 70 and x_c < 110 and y_c > 550 and y_c < 620 and one2==True):
                run("""            
                            use_bpm 123

                            sample "C:/Users/Nathan/Documents/GitHub/Projet-Musique/Projet-Musique/PrEi4/samples/Better.wav"              
                        """)
                run("""live_loop :foo do
                                                                              use_real_time
                                                                              a, b, c, d = sync "/osc/trigger/mod_fm"
                                                                              synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                                                            end """)
                one2 = False
            if (x_c > 120 and x_c < 160 and y_c > 550 and y_c < 620 and one3==True):
                run("""
                        use_bpm 123

                        sample "C:/Users/Nathan/Documents/GitHub/Projet-Musique/Projet-Musique/PrEi4/samples/Faster.wav"
                        """)

                run("""live_loop :foo do
                                                              use_real_time
                                                              a, b, c, d = sync "/osc/trigger/mod_fm"
                                                              synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                                            end """)
                one3 = False
            if (x_c > 170 and x_c < 210 and y_c > 550 and y_c < 620 and one4==True):
                run("""
                        use_bpm 123

                        sample "C:/Users/Nathan/Documents/GitHub/Projet-Musique/Projet-Musique/PrEi4/samples/Stronger.wav"
                        """)

                run("""live_loop :foo do
                                                              use_real_time
                                                              a, b, c, d = sync "/osc/trigger/mod_fm"
                                                              synth :mod_fm, note: a, cutoff: b, sustain: c,release: d
                                                            end """)
                one4 = False
            if (y_c < 550 or x_c > 210):
                print("coucou")
                one1 = True
                one2 = True
                one3 = True
                one4 = True

            frame = cv2.flip(frame, 1)

            AffichageNotes()

            text("HARDER", (30, 40))
            text("BETTER", (30, 90))
            text("FASTER", (30, 140))
            text("STRONGER", (30, 190))

            cv2.imshow('FRAME', frame)
            cv2.imshow('RES', res)

        else:


            frame = cv2.flip(frame, 1)
            txt = cv2.putText(frame, "Pour commencer a jouer, dispose le bouchon devant toi !", (100, 200), 2, 1 / 2, (255, 0, 0), 2, cv2.LINE_4)
            cv2.imshow('FRAME', frame)
            cv2.imshow('RES', res)


        k = cv2.waitKey(5) & 0xFF
        if k == 5:
            break
stop()
cv2.destroyAllWindows()
cap.release()
