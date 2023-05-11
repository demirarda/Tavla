
from texttable import Texttable
import os
import random
import time
import sys
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


table = Texttable()


# oyunun ana yapısı için classlar oluşturuldu

class Gamer:
    tasdegeri="X"
    isturn = False
    turnright = 0
    outgameflake=0
    homeflake=5
    ilkzar = 0
    oyunzari1=3
    oyunzari2=1
    brokenflake = 0
    pickfrom = "A0"
    toplay = "A1"
    outflakes = 0  # dışarı toplanan taşlar


class Flake:
    isbroken = False
    isalone = False


X1oyuncusu = Gamer()
X1oyuncusu.tasdegeri="X"
Y1oyuncusu = Gamer()
Y1oyuncusu.tasdegeri="Y"
aktifoyuncu = Gamer()
zar1 = None
zar2 = 1
alinanharf="a"
gidiciharf="b"

# tablo oluşturuldu

anadict = {"A0": "5X", "A1": "0", "A2": "0", "A3": "0", "A4": "3Y", "A5": "0", "A6": "5Y", "A7": "0", "A8": "0",
           "A9": "0", "A10": "0", "A11": "2X",
           "B0": "5Y", "B1": "0", "B2": "0", "B3": "0", "B4": "3X", "B5": "0", "B6": "5X", "B7": "0", "B8": "0",
           "B9": "0", "B10": "0", "B11": "2Y"}


liste = [["A0", "A1", "A2", "A3", "A4", "A5",  "A6", "A7", "A8", "A9", "A10", "A11"],



         [anadict["A0"], anadict["A1"], anadict["A2"], anadict["A3"], anadict["A4"], anadict["A5"],
          anadict["A6"], anadict["A7"], anadict["A8"], anadict["A9"], anadict["A10"], anadict["A11"]],

         ["", "", "", "", "Broken Flake of X "+str(X1oyuncusu.brokenflake), "Dice1",  "Dice 2 ", "Broken Flake of Y "+str(Y1oyuncusu.brokenflake),
          "", "", "", ""],




         [anadict["B0"], anadict["B1"], anadict["B2"], anadict["B3"], anadict["B4"], anadict["B5"],
          anadict["B6"], anadict["B7"], anadict["B8"], anadict["B9"], anadict["B10"], anadict["B11"]],




         ["B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B11"]

         ]

table.set_cols_align(["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"])
table.set_cols_valign(["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"])
col_len = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
table.set_cols_width(col_len)
table.add_rows(liste)



def ilkzaratilsin():
    global liste
    print("X oyuncusu zar atiyor")

    X1oyuncusu.ilkzar=random.randint(1,6)
    print("X oyuncusu "+ str(X1oyuncusu.ilkzar)+" attı")

    print("Y oyuncusu zar atiyor")

    Y1oyuncusu.ilkzar=random.randint(1,6)

    f = open("Dices.txt", "a")
    f.write(str(X1oyuncusu.ilkzar) + "\n")
    f.write(str(Y1oyuncusu.ilkzar) + "\n")
    f.close()
    print("Y oyuncusu "+ str(Y1oyuncusu.ilkzar)+" attı" )
    if X1oyuncusu.ilkzar > Y1oyuncusu.ilkzar:
        print("X oyuncusu daha büyük attı oyuna X başlayacak")
        X1oyuncusu.isturn=True
        Y1oyuncusu.isturn=False
        liste[2][5] = "Dice1      " + str(X1oyuncusu.ilkzar)
        liste[2][6] = "Dice2      " + str(Y1oyuncusu.ilkzar)
        liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
        liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
        table.reset()
        table.add_rows(liste)
        print(table.draw())
        zarsalla(X1oyuncusu)
    elif Y1oyuncusu.ilkzar > X1oyuncusu.ilkzar:
        print("Y oyuncusu daha büyük attı oyuna Y başlayacak")
        X1oyuncusu.isturn=False
        Y1oyuncusu.isturn=True
        liste[2][5] = "Dice1      " + str(X1oyuncusu.ilkzar)
        liste[2][6] = "Dice2      " + str(Y1oyuncusu.ilkzar)
        liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
        liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
        table.reset()
        table.add_rows(liste)
        print(table.draw())
        zarsalla(Y1oyuncusu)
    else:
        print("Zarlar şans eseri eşit geldi tekrar zar atılacak !!!")
        liste[2][5] = "Dice1      " + str(X1oyuncusu.ilkzar)
        liste[2][6] = "Dice2      " + str(Y1oyuncusu.ilkzar)
        table.reset()
        table.add_rows(liste)
        ilkzaratilsin()

def cikisfonksiyonu(i):

    f = open("continue.txt", "w")
    f.write(anadict["A0"] + "\n")
    f.write(anadict["A1"] + "\n")
    f.write(anadict["A2"] + "\n")
    f.write(anadict["A3"] + "\n")
    f.write(anadict["A4"] + "\n")
    f.write(anadict["A5"] + "\n")
    f.write(anadict["A6"] + "\n")
    f.write(anadict["A7"] + "\n")
    f.write(anadict["A8"] + "\n")
    f.write(anadict["A9"] + "\n")
    f.write(anadict["A10"] + "\n")
    f.write(anadict["A11"] + "\n")
    f.write(anadict["B0"] + "\n")
    f.write(anadict["B1"] + "\n")
    f.write(anadict["B2"] + "\n")
    f.write(anadict["B3"] + "\n")
    f.write(anadict["B4"] + "\n")
    f.write(anadict["B5"] + "\n")
    f.write(anadict["B6"] + "\n")
    f.write(anadict["B7"] + "\n")
    f.write(anadict["B8"] + "\n")
    f.write(anadict["B9"] + "\n")
    f.write(anadict["B10"] + "\n")
    f.write(anadict["B11"] + "\n")

    f.write(str(aktifsira().oyunzari1) + "\n")
    f.write(str(aktifsira().oyunzari2) + "\n")
    f.write(str(aktifsira().brokenflake) + "\n")
    f.write(str(aktifsira().outflakes) + "\n")
    f.write(str(i) + "\n")
    f.write(str(rakipoyuncu().brokenflake) + "\n")
    f.write(str(rakipoyuncu().outflakes) + "\n")
    f.write(str(aktifsira().tasdegeri) + "\n")

    f.close()
    sys.exit()

def tasinyerinidegistir(Gamer,aktifzar,i):

    ilkzarim = Gamer.oyunzari1
    ikincizarim = Gamer.oyunzari2
    print(str(aktifzar) + " zarı icin hangi tasi oynatmak istiyorsunuz -------- bu eli pas geçmek için 'p' yazın -------------------  oyundan çıkmak için 'q' yazın")
    girdi = input()
    liste[2][9] = "Turn of : " + str(aktifsira().tasdegeri)
    global ilkindex2
    global ikinciindex2



    if (girdi == "p" or girdi=="P"):
        return False
    
    elif (girdi=="q" or girdi=="Q"):
        cikisfonksiyonu(i)
    elif(girdi=="" or girdi == " " or len(girdi) not in [2,3] or girdi[0] not in ["A","B"] or girdi[1] not in ["0","1","2","3","4","5","6","7","8","9"] or girdi[-1] not in ["0","1","2","3","4","5","6","7","8","9"]):
        print("hatalı girdi")
        tasinyerinidegistir(aktifsira(),aktifzar,i)
    else:
        Gamer.pickfrom=girdi
    if (Gamer.pickfrom[0]!="A" and Gamer.pickfrom[0]!="B"):
        print("Hatalı seçim yaptınız A0 - B3 - A9 şeklinde seçim yapınız")
        tasinyerinidegistir(aktifsira(), aktifzar,i)

    elif(anadict[Gamer.pickfrom]=="0" or anadict[Gamer.pickfrom][-1]!=Gamer.tasdegeri):
        print("Burada Size Ait Tas Yok Lütfen Tekrar secim yapiniz")
        tasinyerinidegistir(aktifsira(),aktifzar,i)
    elif (anadict[Gamer.pickfrom][-1]=="Y" and (Gamer.pickfrom[0])=="A" and int(Gamer.pickfrom[1:])+aktifzar>=12):

            print("Buraya Oynayamazsiniz")
            tasinyerinidegistir(aktifsira(),aktifzar,i)
    elif (anadict[Gamer.pickfrom][-1]=="X" and (Gamer.pickfrom[0])=="B" and int(Gamer.pickfrom[1:])+aktifzar>=12):

            print("Buraya Oynayamazsiniz")
            tasinyerinidegistir(aktifsira(),aktifzar,i)






    else:




        if(Gamer.tasdegeri=="X"):
            if ((Gamer.pickfrom[0])=="B"):
                Gamer.toplay = ("B" + str(int(Gamer.pickfrom[1:]) + aktifzar))
                if((anadict[("B"+str(int(Gamer.pickfrom[1:])+aktifzar))]=="0" or anadict[("B"+str(int(Gamer.pickfrom[1:])+aktifzar))][1:]=="X") and (anadict[Gamer.pickfrom][-1]=="X")):

                    print("hamle basarili")
                    sifirtoplayici()
                    if (anadict[Gamer.pickfrom][0:-1] == "1"):

                        anadict[Gamer.pickfrom] = "0"
                    else:
                        anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri # tas alinanyerden taş eksiltildi
                    if Gamer.pickfrom[0] == "A":

                        sifirtoplayici()
                        liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)
                    elif Gamer.pickfrom[0] == "B":

                        sifirtoplayici()
                        liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)

                    if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                        anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0]) + 1) + Gamer.tasdegeri
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()
                    else:
                        anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0:-1]) + 1) + anadict[Gamer.toplay][-1]  # taş eklenen yerin güncellemesi2
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "a")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()


                #taş kırılması
                elif (anadict[Gamer.toplay][1:] == "Y" and anadict[Gamer.toplay][0:-1] == "1"):
                    rakipoyuncu().brokenflake += 1
                    print("rakip taşı kırdınız")
                    if (anadict[Gamer.pickfrom][0:-1] == "1"):

                        anadict[Gamer.pickfrom] = "0"
                    else:
                        anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri # tas alinanyerden taş eksiltildi
                    if Gamer.pickfrom[0] == "A":

                        sifirtoplayici()
                        liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)
                    elif Gamer.pickfrom[0] == "B":

                        sifirtoplayici()
                        liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)

                    if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                        anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()

                    else:
                        anadict[Gamer.toplay] = "0"
                        anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri # taş eklenen yerin güncellemesi2
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()



                else:
                    print("hamle basarisiz")
                    tasinyerinidegistir(aktifsira(), aktifzar,i)



            elif ((Gamer.pickfrom[0])=="A"):
                Gamer.toplay = ("A" + str(int(Gamer.pickfrom[1:]) - aktifzar))
                if(int(Gamer.pickfrom[1:])-aktifzar>=0):  #A4 ten A2 ye oynamak örneğin
                    if ((anadict[("A" + str(int(Gamer.pickfrom[1:]) - aktifzar))] == "0" or anadict[("A" + str(int(Gamer.pickfrom[1:]) - aktifzar))][1:] == "X") and (anadict[Gamer.pickfrom][-1] == "X")):
                        print("hamle gayet basarili")
                        sifirtoplayici()

                        if (anadict[Gamer.pickfrom][0:-1] == "1"):

                            anadict[Gamer.pickfrom] = "0"
                        else:
                            anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri # tas alinanyerden taş eksiltildi
                        if Gamer.pickfrom[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                            table.reset()
                            table.add_rows(liste)
                        elif Gamer.pickfrom[0] == "B":

                            sifirtoplayici()

                            liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                            table.reset()
                            table.add_rows(liste)
                        Gamer.toplay = ("A" + str(int(Gamer.pickfrom[1:]) - aktifzar))
                        if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                            anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0]) + 1) + Gamer.tasdegeri
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()

                        else:
                            anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0:-1]) + 1) + anadict[Gamer.toplay][-1]  # taş eklenen yerin güncellemesi2
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()

                    elif (anadict[Gamer.toplay][1:] == "Y" and anadict[Gamer.toplay][0:-1] == "1"):
                        rakipoyuncu().brokenflake += 1
                        print("rakip taşı kırdınız")
                        if (anadict[Gamer.pickfrom][0:-1] == "1"):

                            anadict[Gamer.pickfrom] = "0"
                        else:
                            anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri # tas alinanyerden taş eksiltildi
                        if Gamer.pickfrom[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                            table.reset()
                            table.add_rows(liste)
                        elif Gamer.pickfrom[0] == "B":

                            sifirtoplayici()

                            liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                            table.reset()
                            table.add_rows(liste)
                        Gamer.toplay = ("A" + str(int(Gamer.pickfrom[1:]) - aktifzar))
                        if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                            anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()

                        else:
                            anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri  # taş eklenen yerin güncellemesi2
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()

                    else:
                        print("hamle 1 basarisiz")
                        tasinyerinidegistir(aktifsira(), aktifzar,i)
                else:
                    Gamer.toplay = ("B" + str(abs(int(Gamer.pickfrom[1:]) - aktifzar + 1)))
                    if ((anadict[("B" + str(abs(int(Gamer.pickfrom[1:]) - aktifzar + 1)))] == "0" or anadict[("B" + str(abs(int(Gamer.pickfrom[1:]) - aktifzar + 1)))][1:] == "X") and (anadict[Gamer.pickfrom][-1] == "X")):
                        print("hamle cok basarili")
                        sifirtoplayici()

                        if (anadict[Gamer.pickfrom][0:-1] == "1"):

                            anadict[Gamer.pickfrom] = "0"
                        else:
                            anadict[Gamer.pickfrom] = str(
                                (int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri # tas alinanyerden taş eksiltildi

                        if Gamer.pickfrom[0] == "A":

                            sifirtoplayici()
                            liste[1][(int(Gamer.pickfrom[1:]))] = anadict[Gamer.pickfrom]
                            table.reset()
                            table.add_rows(liste)
                        elif Gamer.pickfrom[0] == "B":

                            sifirtoplayici()
                            liste[3][(int(Gamer.pickfrom[1:]))] = anadict[Gamer.pickfrom]
                            table.reset()
                            table.add_rows(liste)


                        if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                            anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0]) + 1) + Gamer.tasdegeri
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][(int(Gamer.toplay[1:]))] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][(int(Gamer.toplay[1:]))] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()

                        else:
                            anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0:-1]) + 1) + anadict[Gamer.toplay][
                                -1]  # taş eklenen yerin güncellemesi2
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][(int(Gamer.toplay[1:]))] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][(int(Gamer.toplay[1:]))] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()

                    elif (anadict[Gamer.toplay][1:] == "Y" and anadict[Gamer.toplay][0:-1] == "1"):
                        rakipoyuncu().brokenflake += 1
                        print("rakip taşı kırdınız")
                        if (anadict[Gamer.pickfrom][0:-1] == "1"):

                            anadict[Gamer.pickfrom] = "0"
                        else:
                            anadict[Gamer.pickfrom] = str(
                                (int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri  # tas alinanyerden taş eksiltildi

                        if Gamer.pickfrom[0] == "A":

                            sifirtoplayici()
                            liste[1][(int(Gamer.pickfrom[1:]))] = anadict[Gamer.pickfrom]
                            table.reset()
                            table.add_rows(liste)
                        elif Gamer.pickfrom[0] == "B":

                            sifirtoplayici()
                            liste[3][(int(Gamer.pickfrom[1:]))] = anadict[Gamer.pickfrom]
                            table.reset()
                            table.add_rows(liste)

                        if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                            anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][(int(Gamer.toplay[1:]))] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][(int(Gamer.toplay[1:]))] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()

                        else:
                            anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri # taş eklenen yerin güncellemesi2
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][(int(Gamer.toplay[1:]))] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][(int(Gamer.toplay[1:]))] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()

                    else:
                        print("hamle olumcul basarisiz")
                        tasinyerinidegistir(aktifsira(), aktifzar,i)









        else:
            if((Gamer.pickfrom[0])=="B"):
                if(int(Gamer.pickfrom[1:])-aktifzar>=0):
                    Gamer.toplay = ("B" + str(int(Gamer.pickfrom[1:]) - aktifzar))
                    if ((anadict[("B" + str(int(Gamer.pickfrom[1:]) - aktifzar))] == "0" or anadict[("B" + str(int(Gamer.pickfrom[1:]) - aktifzar))][1:] == "Y") and (anadict[Gamer.pickfrom][-1] == "Y")):
                        print("hamle gayet basarili")
                        sifirtoplayici()

                        if (anadict[Gamer.pickfrom][0:-1] == "1"):

                            anadict[Gamer.pickfrom] = "0"
                        else:
                            anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri
                          # tas alinanyerden taş eksiltildi
                        print(anadict[Gamer.pickfrom])
                        if Gamer.pickfrom[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                            table.reset()
                            table.add_rows(liste)
                        elif Gamer.pickfrom[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                            table.reset()
                            table.add_rows(liste)

                        if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                            anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0]) + 1) + Gamer.tasdegeri
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()

                        else:
                            anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0:-1]) + 1) + Gamer.tasdegeri  # taş eklenen yerin güncellemesi2
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()

                    elif (anadict[Gamer.toplay][1:] == "X" and anadict[Gamer.toplay][0:-1] == "1"):
                        rakipoyuncu().brokenflake += 1
                        print("rakip taşı kırdınız")
                        if (anadict[Gamer.pickfrom][0:-1] == "1"):

                            anadict[Gamer.pickfrom] = "0"
                        else:
                            anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri# tas alinanyerden taş eksiltildi
                        print(anadict[Gamer.pickfrom])
                        if Gamer.pickfrom[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                            table.reset()
                            table.add_rows(liste)
                        elif Gamer.pickfrom[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                            table.reset()
                            table.add_rows(liste)

                        if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                            anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()

                        else:
                            anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri  # taş eklenen yerin güncellemesi2
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()

                    else:
                        print("hamle 1 basarisiz")
                        tasinyerinidegistir(aktifsira(), aktifzar,i)


                else:

                    Gamer.toplay = ("A" + str(abs(int(Gamer.pickfrom[1:]) - aktifzar + 1)))

                    if((anadict[("A" + str(abs(int(Gamer.pickfrom[1:]) - aktifzar + 1)))] == "0" or anadict[("A" + str(abs(int(Gamer.pickfrom[1:]) - aktifzar + 1)))][1:] == "Y") and (anadict[Gamer.pickfrom][-1] == "Y")):

                        print("hamle cok basarili")
                        sifirtoplayici()
                        Gamer.toplay=("A" + str(abs(int(Gamer.pickfrom[1:]) - aktifzar + 1)))
                        if (anadict[Gamer.pickfrom][0:-1] == "1"):

                            anadict[Gamer.pickfrom] = "0"
                        else:
                            anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri  # tas alinanyerden taş eksiltildi
                        print(anadict[Gamer.pickfrom])
                        if Gamer.pickfrom[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                            table.reset()
                            table.add_rows(liste)
                        elif Gamer.pickfrom[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                            table.reset()
                            table.add_rows(liste)

                        if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                            anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0]) + 1) + Gamer.tasdegeri
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()

                        else:
                            anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0:-1]) + 1) + Gamer.tasdegeri  # taş eklenen yerin güncellemesi2
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()

                    elif (anadict[Gamer.toplay][-1] == "X" and anadict[Gamer.toplay][0:-1] == "1"):
                        rakipoyuncu().brokenflake += 1
                        print("rakip taşı kırdınız")
                        if (anadict[Gamer.pickfrom][0:-1] == "1"):

                            anadict[Gamer.pickfrom] = "0"
                        else:
                            anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri  # tas alinanyerden taş eksiltildi
                        print(anadict[Gamer.pickfrom])
                        if Gamer.pickfrom[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()
                        elif Gamer.pickfrom[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()

                        if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                            anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()

                        else:
                            anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri  # taş eklenen yerin güncellemesi2
                            if Gamer.toplay[0] == "A":

                                sifirtoplayici()
                                liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                            elif Gamer.toplay[0] == "B":

                                sifirtoplayici()
                                liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                                table.reset()
                                table.add_rows(liste)
                                print(table.draw())
                                f = open("Table.txt", "w")
                                f.write(str(table.draw()) + "\n")
                                f.write(" " + "\n")
                                f.close()
                    else:
                        print("hamle olumcul basarisiz")
                        tasinyerinidegistir(aktifsira(), aktifzar,i)
            else:
                Gamer.toplay = ("A" + str(int(Gamer.pickfrom[1:]) + aktifzar))
                if((anadict[("A"+str(int(Gamer.pickfrom[1:])+aktifzar))]=="0" or anadict[("A"+str(int(Gamer.pickfrom[1:])+aktifzar))][1:]=="Y") and (anadict[Gamer.pickfrom][-1]=="Y")):
                    print("hamle basarili")
                    sifirtoplayici()

                    if (anadict[Gamer.pickfrom][0:-1] == "1"):

                        anadict[Gamer.pickfrom] = "0"
                    else:
                        anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri  # tas alinanyerden taş eksiltildi
                    print(anadict[Gamer.pickfrom])
                    if Gamer.pickfrom[0] == "A":

                        sifirtoplayici()
                        liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)

                    elif Gamer.pickfrom[0] == "B":

                        sifirtoplayici()
                        liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)


                    if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                        anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0]) + 1) + Gamer.tasdegeri
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()

                    else:
                        anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0:-1]) + 1) + anadict[Gamer.toplay][-1]  # taş eklenen yerin güncellemesi2
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()
                elif (anadict[Gamer.toplay][1:] == "X" and anadict[Gamer.toplay][0:-1] == "1"):
                    rakipoyuncu().brokenflake += 1
                    print("rakip taşı kırdınız")
                    if (anadict[Gamer.pickfrom][0:-1] == "1"):

                        anadict[Gamer.pickfrom] = "0"
                    else:
                        anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri  # tas alinanyerden taş eksiltildi
                    print(anadict[Gamer.pickfrom])
                    if Gamer.pickfrom[0] == "A":

                        sifirtoplayici()
                        liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)

                    elif Gamer.pickfrom[0] == "B":

                        sifirtoplayici()
                        liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)


                    if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                        anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()

                    else:
                        anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri  # taş eklenen yerin güncellemesi2
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                            f = open("Table.txt", "w")
                            f.write(str(table.draw()) + "\n")
                            f.write(" " + "\n")
                            f.close()
                else:
                    print("hamle basarisiz")
                    tasinyerinidegistir(aktifsira(), aktifzar,i)

def disaricikarma(Gamer,aktifzar):
    liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
    liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
    liste[2][9] = "Turn of : " + str(aktifsira().tasdegeri)
    print(str(aktifzar)+ " oynamak için yer seçiniz 1-2-5 ŞEKLİNDE SEÇİM YAPINIZ  ")
    Gamer.pickfrom = input()
    if (Gamer.pickfrom[0]!="A" and Gamer.pickfrom[0]!="B"):
        print("Hatalı seçim yaptınız A0 - B3 - A9 şeklinde seçim yapınız")
        disaricikarma(aktifsira(), aktifzar)
    elif (anadict[Gamer.pickfrom] == "0" or anadict[Gamer.pickfrom][-1] != Gamer.tasdegeri):
        print("Burada Size Ait Tas Yok Lütfen Tekrar secim yapiniz")
        disaricikarma(aktifsira(), aktifzar)
    elif (Gamer.pickfrom=="" or Gamer.pickfrom==" "):
        print("Hatalı seçim yaptınız A0 - B3 - A9 şeklinde seçim yapınız")
        disaricikarma(aktifsira(), aktifzar)
    else:

        if(Gamer.tasdegeri=="X"):
            if(int(int(Gamer.pickfrom[1:])+aktifzar)<=11):
                Gamer.toplay=("B"+str(int(Gamer.pickfrom[1:])+aktifzar))
                if(anadict[Gamer.toplay]=="0" or anadict[Gamer.toplay][1:]=="X"):
                    if (anadict[Gamer.pickfrom][0:-1] == "1"):

                        anadict[Gamer.pickfrom] = "0"
                    else:
                        anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri  # tas alinanyerden taş eksiltildi
                    if Gamer.pickfrom[0] == "A":

                        sifirtoplayici()
                        liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)

                    elif Gamer.pickfrom[0] == "B":

                        sifirtoplayici()
                        liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)

                    if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                        anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0]) + 1) + Gamer.tasdegeri
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())

                    else:
                        anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0:-1]) + 1) + Gamer.tasdegeri # taş eklenen yerin güncellemesi2
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())

                elif(anadict[Gamer.toplay]=="1Y"):
                    rakipoyuncu().brokenflake+=1
                    if (anadict[Gamer.pickfrom][0:-1] == "1"):

                        anadict[Gamer.pickfrom] = "0"
                    else:
                        anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri  # tas alinanyerden taş eksiltildi
                    if Gamer.pickfrom[0] == "A":

                        sifirtoplayici()
                        liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)

                    elif Gamer.pickfrom[0] == "B":

                        sifirtoplayici()
                        liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)


                    if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                        anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())

                    else:
                        anadict[Gamer.toplay] = "0"
                        anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri  # taş eklenen yerin güncellemesi2
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                else:
                    print("hatalı seçim")
                    disaricikarma(aktifsira(),aktifzar)


            else:
                print("taşınız oyun dışına çıktı")
                aktifsira().outflakes+=1
                aktifsira().homeflake+=1
                if (anadict[Gamer.pickfrom][0:-1] == "1"):

                    anadict[Gamer.pickfrom] = "0"
                else:
                    anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri  # tas alinanyerden taş eksiltildi
                if Gamer.pickfrom[0] == "A":

                    sifirtoplayici()
                    liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                    table.reset()
                    table.add_rows(liste)
                    print(table.draw())
                elif Gamer.pickfrom[0] == "B":

                    sifirtoplayici()
                    liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                    table.reset()
                    table.add_rows(liste)
                    print(table.draw())

        else:
            if(int(int(Gamer.pickfrom[1:])+aktifzar)<=11):
                Gamer.toplay=("A"+str(int(Gamer.pickfrom[1:])+aktifzar))
                if(anadict[Gamer.toplay]=="0" or anadict[Gamer.toplay][1:]=="Y"):
                    if (anadict[Gamer.pickfrom][0:-1] == "1"):

                        anadict[Gamer.pickfrom] = "0"
                    else:anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri# tas alinanyerden taş eksiltildi
                    print(anadict[Gamer.pickfrom])
                    if Gamer.pickfrom[0] == "A":

                        sifirtoplayici()
                        liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)

                    elif Gamer.pickfrom[0] == "B":

                        sifirtoplayici()
                        liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)


                    if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                        anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0]) + 1) + Gamer.tasdegeri
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())

                    else:
                        anadict[Gamer.toplay] = str(int(anadict[Gamer.toplay][0:-1]) + 1) + Gamer.tasdegeri  # taş eklenen yerin güncellemesi2
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())




                elif(anadict[Gamer.toplay]=="1X"):
                    rakipoyuncu().brokenflake += 1
                    print("rakip taşı kırdınız")
                    if (anadict[Gamer.pickfrom][0:-1] == "1"):

                        anadict[Gamer.pickfrom] = "0"
                    else:
                        anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri  # tas alinanyerden taş eksiltildi
                    print(anadict[Gamer.pickfrom])
                    if Gamer.pickfrom[0] == "A":

                        sifirtoplayici()
                        liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)

                    elif Gamer.pickfrom[0] == "B":

                        sifirtoplayici()
                        liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                        table.reset()
                        table.add_rows(liste)


                    if anadict[Gamer.toplay] == "0":  # taş eklenen yerin güncellemesi
                        anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())

                    else:
                        anadict[Gamer.toplay] = str(1) + Gamer.tasdegeri  # taş eklenen yerin güncellemesi2
                        if Gamer.toplay[0] == "A":

                            sifirtoplayici()
                            liste[1][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                        elif Gamer.toplay[0] == "B":

                            sifirtoplayici()
                            liste[3][int(Gamer.toplay[1:])] = anadict[Gamer.toplay]
                            table.reset()
                            table.add_rows(liste)
                            print(table.draw())
                else:
                    print("hatalı seçim yapıldı bir daha seçin")
                    disaricikarma(aktifsira(),aktifzar)
            else:
                print("taşınız oyun dışına çıktı")
                aktifsira().outflakes += 1
                aktifsira().homeflake += 1
                if (anadict[Gamer.pickfrom][0:-1] == "1"):

                    anadict[Gamer.pickfrom] = "0"
                else:
                    anadict[Gamer.pickfrom] = str((int(float(anadict[Gamer.pickfrom][0:-1])) - 1)) + Gamer.tasdegeri  # tas alinanyerden taş eksiltildi
                if Gamer.pickfrom[0] == "A":

                    sifirtoplayici()
                    liste[1][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                    table.reset()
                    table.add_rows(liste)
                    print(table.draw())
                elif Gamer.pickfrom[0] == "B":

                    sifirtoplayici()
                    liste[3][int(Gamer.pickfrom[1:])] = anadict[Gamer.pickfrom]
                    table.reset()
                    table.add_rows(liste)
                    print(table.draw())

def gameover():
    file = open("continue.txt", "w")
    file.close()
    file = open("Dices.txt", "w")
    file.close()
    file = open("Table.txt", "w")
    file.close()
    if(X1oyuncusu.outflakes==15):

        print("oyun bitti ve x kazandı")
    else:
        print("oyun bitti ve y kazandı")
    sys.exit()

def anakontroller(Gamer,zarlar):
        global table
        global liste
        liste[2][9] = "Turn of : " + str(aktifsira().tasdegeri)
        i=0
        while i != aktifsira().turnright:
            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
            table.reset()
            table.add_rows(liste)
            homeflakex()
            if(aktifsira().brokenflake!=0):

                if(len(zarlar)==2):
                    print(str(aktifsira().brokenflake) + " adet kırık taşınız var")
                    deger=(input("Hangi zar için oynayacaksın ----- hak eksiltmek için p yazın"))
                    if str(deger)=="q" or str(deger)=="Q":
                        cikisfonksiyonu(i)
                    elif str(deger)=="p" or str(deger)=="P":
                        liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                        liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                        table.reset()
                        table.add_rows(liste)
                        i+=1

                        print("bir hakkınızı geçtiniz")
                    elif str(deger) == "" or str(deger) == " " or deger not in ["1","2","3","4","5","6"] :
                        print("hatalı girdi")
                        anakontroller(aktifsira(), zarlar)
                    elif(int(deger) in zarlar):
                        aktifzar=int(deger)
                        
                        if(kiriktasoynama(aktifsira(),aktifzar)):
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            zarlar.remove(aktifzar)
                            i+=1

                        else:
                            print("bu el giremediniz")

                else:
                    print(str(aktifsira().brokenflake) + " adet kırık taşınız var")
                    deger=(input("Hangi zar için oynayacaksın ----- hak eksiltmek için p yazın"))
                    if str(deger)=="p" or str(deger)=="P":
                        print("bir hakkınızı geçtiniz")

                        i+=1
                    elif str(deger)=="" or str(deger)==" ":
                        print("hatalı girdi")
                        anakontroller(aktifsira(),zarlar)
                    elif(int(deger) in zarlar):
                        aktifzar=int(deger)
                        
                        if(kiriktasoynama(aktifsira(),aktifzar)):
                            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                            table.reset()
                            table.add_rows(liste)
                            i += 1

                            zarlar.remove(aktifzar)
                        else:
                            print("bu el oyuna giremediniz")

                            aktifsira().turnright = 0
                            rakipoyuncu().turnright = 0
                            deaktifsira().isturn = True
                            zarsalla(aktifsira())

            elif(aktifsira().homeflake+aktifsira().outflakes==15):
                if(aktifsira().outflakes==15):
                    gameover()
                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                table.reset()
                table.add_rows(liste)
                aktifzar=zarlar[0]
                (disaricikarma(aktifsira(),aktifzar))

                i += 1

                zarlar.remove(zarlar[0])

            else:
                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                table.reset()
                table.add_rows(liste)
                aktifzar = zarlar[0]
                tasinyerinidegistir(aktifsira(),aktifzar,i)
                i += 1
                zarlar.remove(zarlar[0])
            liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
            liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
            table.reset()
            table.add_rows(liste)
        aktifsira().turnright=0
        rakipoyuncu().turnright=0
        deaktifsira().isturn = True
        zarsalla(aktifsira())

def rakipoyuncu():
    if X1oyuncusu.isturn==False:
        return X1oyuncusu
    else: return Y1oyuncusu

def deaktifsira():
    if X1oyuncusu.isturn==True:
        X1oyuncusu.isturn=False
        return Y1oyuncusu
    else:
        Y1oyuncusu.isturn=False
        return X1oyuncusu

def homeflakex():
    X1oyuncusu.homeflake=0
    Y1oyuncusu.homeflake=0
    if(anadict["B6"][1:]=="X"):
        X1oyuncusu.homeflake += int(anadict["B6"][0:-1])
    if(anadict["B7"][1:]=="X"):
        X1oyuncusu.homeflake += int(anadict["B7"][0:-1])
    if(anadict["B8"][1:]=="X"):
        X1oyuncusu.homeflake += int(anadict["B8"][0:-1])
    if(anadict["B9"][1:]=="X"):
        X1oyuncusu.homeflake += int(anadict["B9"][0:-1])
    if(anadict["B10"][1:]=="X"):
        X1oyuncusu.homeflake += int(anadict["B10"][0:-1])
    if(anadict["B11"][1:]=="X"):
        X1oyuncusu.homeflake += int(anadict["B11"][0:-1])
    if(anadict["A6"][1:]=="Y"):
        Y1oyuncusu.homeflake += int(anadict["A6"][0:-1])
    if(anadict["A7"][1:]=="Y"):
        Y1oyuncusu.homeflake += int(anadict["A7"][0:-1])
    if(anadict["A8"][1:]=="Y"):
        Y1oyuncusu.homeflake += int(anadict["A8"][0:-1])
    if(anadict["A9"][1:]=="Y"):
        Y1oyuncusu.homeflake += int(anadict["A9"][0:-1])
    if(anadict["A10"][1:]=="Y"):
        Y1oyuncusu.homeflake += int(anadict["A10"][0:-1])
    if(anadict["A11"][1:]=="Y"):
        Y1oyuncusu.homeflake += int(anadict["A11"][0:-1])

def aktifsira():
    if X1oyuncusu.isturn == True :
        return X1oyuncusu

    else: return Y1oyuncusu

def kiriktasoynama(Gamer,aktifzar):
    liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
    liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
    liste[2][9] = "Turn of : " + str(aktifsira().tasdegeri)





    if(aktifsira().tasdegeri=="X"):  #x oyuncu için durumlar



            if(anadict["A"+str(12-aktifzar)]=="0" or anadict["A"+str(12-aktifzar)][1:]=="X" ): #girilecek yer boşsa ya da kendi taşımız varsa
                    aktifsira().brokenflake-=1
                    print("kırık taş oyuna girildi")
                    anadict["A" + str(12 - aktifzar)] = str(int(anadict["A" + str(12 - aktifzar)][0])+1)+"X"
                    liste[1][12 - aktifzar] = anadict["A" + str(12 - aktifzar)]
                    liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                    liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                    table.reset()
                    table.add_rows(liste)

                    print(table.draw())
                    return True

            elif (anadict["A"+str(12-aktifzar)]=="1Y"): #girilecek yerde rakibin tek taşı varsa
                    print("rakip taşı kırdınız !")
                    rakipoyuncu().brokenflake+=1
                    aktifsira().brokenflake -= 1
                    anadict["A" + str(12 - aktifzar)]="0"
                    anadict["A" + str(12 - aktifzar)] = str(int(anadict["A" + str(12 - aktifzar)][0])+1)+"X"
                    liste[1][12 - aktifzar] = anadict["A" + str(12 - aktifzar)]
                    liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                    liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                    table.reset()
                    table.add_rows(liste)
                    print(table.draw())
                    return True
            else:
                    print("Buraya giremezsiniz")
                    return False
    else:


            print("kırık zar " + str(aktifzar) + " değerinden giriliyor")

            if (anadict["B" + str(12 - aktifzar)] == "0" or anadict["B" + str(12 - aktifzar)][1:] == "Y"):  # girilecek yer boşsa ya da kendi taşımız varsa
                aktifsira().brokenflake -= 1
                print("kırık taş oyuna girildi")
                anadict["B" + str(12 - aktifzar)] = str(int(anadict["B" + str(12 - aktifzar)][0]) + 1) + "Y"
                liste[3][12 - aktifzar] = anadict["B" + str(12 - aktifzar)]
                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                table.reset()
                table.add_rows(liste)
                print(table.draw())
                return True

            elif (anadict["B" + str(12 - aktifzar)] == "1X"):  # girilecek yerde rakibin tek taşı varsa
                print("rakip taşı kırdınız !")
                rakipoyuncu().brokenflake += 1
                aktifsira().brokenflake -= 1
                anadict["B" + str(12 - aktifzar)] = "0"
                anadict["B" + str(12 - aktifzar)] = str(int(anadict["B" + str(12 - aktifzar)][0]) + 1) + "Y"
                liste[3][12 - aktifzar] = anadict["B" + str(12 - aktifzar)]
                liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
                liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
                table.reset()
                table.add_rows(liste)
                print(table.draw())
                return True
            else:
                print("Buraya giremezsiniz")
                return False

def zarsalla(Gamer):

        global liste
        liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
        liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
        liste[2][9] = "Turn of : " + str(aktifsira().tasdegeri)
        print(str(aktifsira().tasdegeri)+" oyuncusu zar atıyor")
        zar1 =random.randint(1,6)
        print("İlk zar "+ str(zar1)+" geldi")
        aktifsira().oyunzari1=zar1

        zar2 =random.randint(1,6)
        print("İkinci zar "+str(zar2)+" geldi")
        aktifsira().oyunzari2 = zar2
        liste[2][5] = "Dice1      " + str(aktifsira().oyunzari1)
        liste[2][6] = "Dice2      " + str(aktifsira().oyunzari2)
        liste[2][4] =  "Broken Flake of X "+str(X1oyuncusu.brokenflake)
        liste[2][7] =  "Broken Flake of Y "+str(Y1oyuncusu.brokenflake)
        table.reset()
        table.add_rows(liste)
        print(table.draw())
        f = open("Dices.txt", "a")
        f.write(str(zar1) + " ")
        f.write(str(zar2) + "\n")
        f.close()
        if zar1==zar2:
            aktifsira().turnright=4
            zarlar = [zar1,zar1,zar2,zar2]
        else :
            aktifsira().turnright=2
            zarlar = [zar1,zar2]
        if Gamer.tasdegeri=="X":
            anakontroller(X1oyuncusu,zarlar)
        else:
            anakontroller(Y1oyuncusu,zarlar)

def oyunabasla():
    print("iki oyuncu icin masa hazırlandı zarlar atılacak")
    ilkzaratilsin()

def devamfonksiyonu():
    global liste
    liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
    liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
    global anadict
    global zarlar
    file1 = open('continue.txt', 'r')
    table.reset()
    Lines = file1.readlines()
    anadict["A0"] = Lines[0][0:-1]
    anadict["A1"] = Lines[1][0:-1]
    anadict["A2"] = Lines[2][0:-1]
    anadict["A3"] = Lines[3][0:-1]
    anadict["A4"] = Lines[4][0:-1]
    anadict["A5"] = Lines[5][0:-1]
    anadict["A6"] = Lines[6][0:-1]
    anadict["A7"] = Lines[7][0:-1]
    anadict["A8"] = Lines[8][0:-1]
    anadict["A9"] = Lines[9][0:-1]
    anadict["A10"] = Lines[10][0:-1]
    anadict["A11"] = Lines[11][0:-1]
    anadict["B0"] = Lines[12][0:-1]
    anadict["B1"] = Lines[13][0:-1]
    anadict["B2"] = Lines[14][0:-1]
    anadict["B3"] = Lines[15][0:-1]
    anadict["B4"] = Lines[16][0:-1]
    anadict["B5"] = Lines[17][0:-1]
    anadict["B6"] = Lines[18][0:-1]
    anadict["B7"] = Lines[19][0:-1]
    anadict["B8"] = Lines[20][0:-1]
    anadict["B9"] = Lines[21][0:-1]
    anadict["B10"] = Lines[22][0:-1]
    anadict["B11"] = Lines[23][0:-1]
    sirakimde = Lines[31][0:-1]
    if(sirakimde=="X"):
        X1oyuncusu.isturn=True
    else:
        Y1oyuncusu.isturn=True
    aktifsira().oyunzari1=int(Lines[24][0:-1])
    aktifsira().oyunzari2=int(Lines[25][0:-1])
    print("sıra " + aktifsira().tasdegeri+" oyuncusunda")
    liste = [["A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11"],

             [anadict["A0"], anadict["A1"], anadict["A2"], anadict["A3"], anadict["A4"], anadict["A5"],
              anadict["A6"], anadict["A7"], anadict["A8"], anadict["A9"], anadict["A10"], anadict["A11"]],

             ["", "", "", "", "Broken Flake of X " + str(X1oyuncusu.brokenflake), "Dice1      "+ str(aktifsira().oyunzari1), "Dice2     "+ str(aktifsira().oyunzari2),
              "Broken Flake of Y " + str(Y1oyuncusu.brokenflake),
              "", "", "", ""],

             [anadict["B0"], anadict["B1"], anadict["B2"], anadict["B3"], anadict["B4"], anadict["B5"],
              anadict["B6"], anadict["B7"], anadict["B8"], anadict["B9"], anadict["B10"], anadict["B11"]],

             ["B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B11"]

             ]

    table.reset()
    table.add_rows(liste)




    aktifsira().brokenflake=int(Lines[26])
    aktifsira().outflakes=int(Lines[27])
    kackezoynadi=int(Lines[28])
    rakipoyuncu().brokenflake=int(Lines[29])
    rakipoyuncu().outflakes=int(Lines[30])
    file1.close()
    liste[2][4] = "Broken Flake of X " + str(X1oyuncusu.brokenflake)
    liste[2][7] = "Broken Flake of Y " + str(Y1oyuncusu.brokenflake)
    table.reset()
    table.add_rows(liste)
    print(table.draw())
    if(aktifsira().oyunzari1==aktifsira().oyunzari2):
        aktifsira().turnright=4-kackezoynadi
        zarlar=[aktifsira().oyunzari1,aktifsira().oyunzari1,aktifsira().oyunzari1,aktifsira().oyunzari1]
        anakontroller(aktifsira(),zarlar)

    else:
        aktifsira().turnright=2-kackezoynadi
        zarlar=[aktifsira().oyunzari1,aktifsira().oyunzari2]
        if(kackezoynadi!=0):
            zarlar.pop(0)
            anakontroller(aktifsira(),zarlar)
        else:
            anakontroller(aktifsira(),zarlar)

def oyunagiris():
    print("Hosgeldiniz")
    print("1-Yeni Oyun ####  2-Kayıtlı oyun yükle")
    secim = input()
    if secim == "1":
        file = open("Dices.txt", "w")
        file.close()
        file = open("Table.txt", "w")
        file.close()
        file = open("continue.txt", "w")
        file.close()
        oyunabasla()
    elif secim=="2":
        file_path = 'continue.txt'
        # check if size of file is 0
        if os.stat(file_path).st_size == 0:
            print('Save File is empty there is no game to load please start a new one')
            oyunagiris()
        else:
            print('File is not empty loading game')
            devamfonksiyonu()
    else:
        print("Incorrect pick")
        oyunagiris()

def sifirtoplayici():
    for i in range(12):
        if(anadict["A"+str(i)]=="0X" or anadict["A"+str(i)]=="0Y"):
            anadict["A" + str(i)] = "0"
            liste[1][i] = anadict["A" + str(i)]
            table.reset()
            table.add_rows(liste)
        elif(anadict["B"+str(i)]=="0X" or anadict["B"+str(i)]=="0Y"):
            anadict["B" + str(i)] = "0"
            liste[3][i] = anadict["B" + str(i)]
            table.reset()
            table.add_rows(liste)
        else:
            break

oyunagiris()