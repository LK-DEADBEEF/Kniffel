from functools import partial

from PyQt5.QtGui import QIcon
from audioplayer import AudioPlayer
from Hauptfenster import *
from spielfenster import *
from Bestenliste import *
import Kniffelclass as kn
from Hilfe import *
import sys
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QScrollBar
from PyQt5.QtCore import Qt,QFile, QTextStream


class hauptmenue(Ui_MainWindow):
    def __init__(self, window):
        super().__init__()
        self.setupUi(window)
        self.barsound = AudioPlayer("barsound.mp3")
        self.barsound.play(loop=True)
        self.pushButton_2.clicked.connect(self.spielclick)
        self.pushButton.clicked.connect(self.help)
        self.pushButton_4.clicked.connect(self.exit)
        self.pushButton_3.clicked.connect(self.besten)
        self.actionneues_spiel.triggered.connect(self.spielclick)
        self.actionProgramm_schliessen.triggered.connect(self.exit)
        self.actionHilfe_Regeln.triggered.connect(self.help)

    def spielclick(self):
        MainWindow1.hide()
        self.barsound.stop()
        MainWindow2.show()

    def help(self):
        MainWindow3.show()


    def besten(self):

        beste.aktualisieren()
        MainWindow4.show()

    def exit(self):
        exit(1)

class help(Ui_Form):
    def __init__(self, window):
        super().__init__()
        self.setupUi(window)

class bestenliste(besten):
    def __init__(self, window):
        super().__init__()
        self.setupUi(window)
        self.namen = [self.name1, self.name2, self.name3, self.name4, self.name5, self.name6, self.name7, self.name8,
                      self.name9, self.name10]
        self.punkte = [self.punkte1, self.punkte2, self.punkte3, self.punkte4, self.punkte5, self.punkte6, self.punkte7,
                       self.punkte8, self.punkte9, self.punkte10]
        self.best = [self.namen, self.punkte]
    def aktualisieren(self):
        self.text = open("Bestenliste.txt")
        self.besten = self.text.readlines()
        self.text.close()
        self.Punkte = []
        self.Namen = []
        for i in range(10):
            getValues = self.besten[i].split()
            self.Namen.append(str(getValues[0]))
            self.Punkte.append(str(getValues[1]))
        for i in range(10):
            exec("self.name{}.setText(self.Namen[{}])".format(i+1,i))
            exec("self.punkte{}.setText(self.Punkte[{}])".format(i+1,i))


class spielmenue(spielfenster):
    def __init__(self, window):
        super().__init__()
        self.setupUi(window)
        self.numplayers = 0  # Anzahl der Spieler
        self.Wurf = 0  # Wie vielter Wurf (1-3)
        self.Runde = 0  # Wie viele Runden wurden gespielt
        self.played = 0  # Hilfsvariable für Menüwechsel, wenn neue Fensterinstanz erstellt wurde
        self.dran = 0  # index für die Liste Spielerliste um zu wissen wer dran ist
        self.Spielerliste = []  # Liste aus Kniffelclassobjekten um Spieler dynamisch anzusteuern
        self.wuerfelbecher = []  # Liste für Würfel die gewürfelt werden sollen
        self.gesichert = []  # Liste für Würfel die gesichert werden sollen
        self.wuerfelsound = AudioPlayer("wuerfelsound.mp3")  # Sound beim Würfeln
        self.winnersound = AudioPlayer("winnersound.mp3")  # Sound beim Popup, wenn Gewinner angezeigt wird
        self.pushButton.clicked.connect(self.zurueck)
        self.pushButtonStart.clicked.connect(self.rungame)
        self.pushButtonwuerfeln.clicked.connect(self.wuerfeln)
        self.pushButtonrestart.clicked.connect(self.restart)
        self.pushButtonwuerfeln.setEnabled(False)
        self.actionHauptmen.triggered.connect(self.zurueck)
        # ab hier werden alle PushButtons einer Spalte, also eines Spielers einer Liste hinzugefügt
        self.buttonsp1 = []
        self.buttonsp1.append(self.pushButtonS1_1)
        self.buttonsp1.append(self.pushButtonS1_2)
        self.buttonsp1.append(self.pushButtonS1_3)
        self.buttonsp1.append(self.pushButtonS1_4)
        self.buttonsp1.append(self.pushButtonS1_5)
        self.buttonsp1.append(self.pushButtonS1_6)
        self.buttonsp1.append(self.pushButtonS1_7)
        self.buttonsp1.append(self.pushButtonS1_8)
        self.buttonsp1.append(self.pushButtonS1_9)
        self.buttonsp1.append(self.pushButtonS1_10)
        self.buttonsp1.append(self.pushButtonS1_11)
        self.buttonsp1.append(self.pushButtonS1_12)
        self.buttonsp1.append(self.pushButtonS1_13)
        self.buttonsp2 = []
        self.buttonsp2.append(self.pushButtonS2_1)
        self.buttonsp2.append(self.pushButtonS2_2)
        self.buttonsp2.append(self.pushButtonS2_3)
        self.buttonsp2.append(self.pushButtonS2_4)
        self.buttonsp2.append(self.pushButtonS2_5)
        self.buttonsp2.append(self.pushButtonS2_6)
        self.buttonsp2.append(self.pushButtonS2_7)
        self.buttonsp2.append(self.pushButtonS2_8)
        self.buttonsp2.append(self.pushButtonS2_9)
        self.buttonsp2.append(self.pushButtonS2_10)
        self.buttonsp2.append(self.pushButtonS2_11)
        self.buttonsp2.append(self.pushButtonS2_12)
        self.buttonsp2.append(self.pushButtonS2_13)
        self.buttonsp3 = []
        self.buttonsp3.append(self.pushButtonS3_1)
        self.buttonsp3.append(self.pushButtonS3_2)
        self.buttonsp3.append(self.pushButtonS3_3)
        self.buttonsp3.append(self.pushButtonS3_4)
        self.buttonsp3.append(self.pushButtonS3_5)
        self.buttonsp3.append(self.pushButtonS3_6)
        self.buttonsp3.append(self.pushButtonS3_7)
        self.buttonsp3.append(self.pushButtonS3_8)
        self.buttonsp3.append(self.pushButtonS3_9)
        self.buttonsp3.append(self.pushButtonS3_10)
        self.buttonsp3.append(self.pushButtonS3_11)
        self.buttonsp3.append(self.pushButtonS3_12)
        self.buttonsp3.append(self.pushButtonS3_13)
        self.buttonsp4 = []
        self.buttonsp4.append(self.pushButtonS4_1)
        self.buttonsp4.append(self.pushButtonS4_2)
        self.buttonsp4.append(self.pushButtonS4_3)
        self.buttonsp4.append(self.pushButtonS4_4)
        self.buttonsp4.append(self.pushButtonS4_5)
        self.buttonsp4.append(self.pushButtonS4_6)
        self.buttonsp4.append(self.pushButtonS4_7)
        self.buttonsp4.append(self.pushButtonS4_8)
        self.buttonsp4.append(self.pushButtonS4_9)
        self.buttonsp4.append(self.pushButtonS4_10)
        self.buttonsp4.append(self.pushButtonS4_11)
        self.buttonsp4.append(self.pushButtonS4_12)
        self.buttonsp4.append(self.pushButtonS4_13)
        self.buttonsp5 = []
        self.buttonsp5.append(self.pushButtonS5_1)
        self.buttonsp5.append(self.pushButtonS5_2)
        self.buttonsp5.append(self.pushButtonS5_3)
        self.buttonsp5.append(self.pushButtonS5_4)
        self.buttonsp5.append(self.pushButtonS5_5)
        self.buttonsp5.append(self.pushButtonS5_6)
        self.buttonsp5.append(self.pushButtonS5_7)
        self.buttonsp5.append(self.pushButtonS5_8)
        self.buttonsp5.append(self.pushButtonS5_9)
        self.buttonsp5.append(self.pushButtonS5_10)
        self.buttonsp5.append(self.pushButtonS5_11)
        self.buttonsp5.append(self.pushButtonS5_12)
        self.buttonsp5.append(self.pushButtonS5_13)
        self.buttonsp6 = []

        self.buttonsp6.append(self.pushButtonS6_1)
        self.buttonsp6.append(self.pushButtonS6_2)
        self.buttonsp6.append(self.pushButtonS6_3)
        self.buttonsp6.append(self.pushButtonS6_4)
        self.buttonsp6.append(self.pushButtonS6_5)
        self.buttonsp6.append(self.pushButtonS6_6)
        self.buttonsp6.append(self.pushButtonS6_7)
        self.buttonsp6.append(self.pushButtonS6_8)
        self.buttonsp6.append(self.pushButtonS6_9)
        self.buttonsp6.append(self.pushButtonS6_10)
        self.buttonsp6.append(self.pushButtonS6_11)
        self.buttonsp6.append(self.pushButtonS6_12)
        self.buttonsp6.append(self.pushButtonS6_13)
        # nun werden alle Listen auf Spalten in eine buttonList verschoben
        # dient als Workaround, weil das grid layout kein setEnabled besitzt, bzw. es nicht so funktioniert wie wir uns
        # das vorgestellt haben
        self.buttonList = [self.buttonsp1, self.buttonsp2, self.buttonsp3,
                           self.buttonsp4, self.buttonsp5, self.buttonsp6]
        self.labelS1 = [self.labelS1_1, self.labelS1_2, self.labelS1_3, self.labelS1_4, self.labelS1_5, self.labelS1_6]
        self.labelS2 = [self.labelS2_1, self.labelS2_2, self.labelS2_3, self.labelS2_4, self.labelS2_5, self.labelS2_6]
        self.labelS3 = [self.labelS3_1, self.labelS3_2, self.labelS3_3, self.labelS3_4,
                        self.labelS3_5, self.labelS3_6]
        self.labelS4 = [self.labelS4_1, self.labelS4_2, self.labelS4_3, self.labelS4_4,
                        self.labelS4_5, self.labelS4_6]
        self.labelS5 = [self.labelS5_1, self.labelS5_2, self.labelS5_3, self.labelS5_4,
                        self.labelS5_5, self.labelS5_6]
        self.labelS6 = [self.labelS6_1, self.labelS6_2, self.labelS6_3, self.labelS6_4,
                        self.labelS6_5, self.labelS6_6]
        self.labellist = [self.labelS1, self.labelS2, self.labelS3, self.labelS4, self.labelS5, self.labelS6]
        # In labellist werden alle Labels der jeweiligen Spieler gespeichert, um diese dynamisch anzusteuern
        for i in range(0,6):
            for j in range(13):
                self.buttonList[i][j].clicked.connect(partial(self.eintragen, action=j))
        self.wuerfellist = [self.wuerfel1, self.wuerfel2, self.wuerfel3, self.wuerfel4, self.wuerfel5]
        # In wuerfellist werden alle wuerfelobjekte gespeichert, die auf dem Grün angezeigt werden,
        # um diese dynamisch anzusteuern
        for i in range(len(self.wuerfellist)):
            self.wuerfellist[i].clicked.connect(partial(self.wuerfelsave, saven=i))
        self.savelist = [self.save1, self.save2, self.save3, self.save4, self.save5]
        for i in range(len(self.savelist)):
            self.savelist[i].clicked.connect(partial(self.wuerfelzurueck, back=i))
        self.namelist = []
        for i in range(self.numplayers - 1, 6):
            for j in range(13):
                self.buttonList[i][j].setEnabled(False)

    def restart(self):
        MainWindow2.destroy()
        self.MainWindow2 = QtWidgets.QMainWindow()
        spiel = spielmenue(MainWindow2)

    def zurueck(self):
        if self.played == 0:
            MainWindow2.hide()
            MainWindow1.show()
        else:
            self.MainWindow2.hide()
            MainWindow1.show()

    def rungame(self):
        spieler = str(self.comboBox.currentText())
        self.numplayers = int(spieler.split()[0])
        self.pushButtonStart.setEnabled(False)
        self.pushButtonrestart.setEnabled(False)
        self.comboBox.setEnabled(False)
        for i in range(0, 6):
            for j in range(13):
                self.buttonList[i][j].setEnabled(False)
        for i in range(1, 6):
            exec("self.wuerfel{}.hide()".format(i))
        self.pushButtonwuerfeln.setEnabled(True)
        self.Wurf = 1
        self.Runde = 1
        self.dran = 1
        self.label_7.setText("Wurf übrig: 3")
        for i in range(1, self.numplayers + 1):
            globals()['player%s' % i] = kn.Kniffel()  # Für jeden Spieler wird eine Klasse mit seinem Namen erstellt
            if i == 1:
                self.Spielerliste.append(player1)
            elif i == 2:
                self.Spielerliste.append(player2)
            elif i == 3:
                self.Spielerliste.append(player3)
            elif i == 4:
                self.Spielerliste.append(player4)
            elif i == 5:
                self.Spielerliste.append(player5)
            elif i == 6:
                self.Spielerliste.append(player6)
        for i in range(self.numplayers):
            for j in range(13):
                self.buttonList[i][j].setText(self.Spielerliste[i].bisherig[j])
            text, result = QInputDialog.getText(self, 'Input Dialog', 'Spieler '+ str(i+1) +' - Geben Sie Ihren Namen ein:')
            self.Spielerliste[i - 1].name = text
            exec("self.label_{}.setText(\"{}\")".format(i + 1, str(text)))
            self.namelist.append(str(text))
        for i in range(1, 6):
            exec("self.wuerfel{}.setEnabled(False)".format(i))
            exec("self.save{}.setEnabled(False)".format(i))
        self.popup()

    def wuerfeln(self):  # abfragen welcher Spieler an der Reihe ist
        # null = 1
        self.label_7.setText("Wurf übrig: "+ str(3-self.Wurf))

        for j in range(13):
            self.buttonList[self.dran - 1][j].setEnabled(True)  # Alle Spieler ausgrauen bis auf den ersten
        if self.Wurf > 1:
            isempty = True
            for i in range(len(self.wuerfelbecher)):
                if self.wuerfelbecher[i] > 0:
                    isempty = False
            if isempty == True:
                msg = QMessageBox()
                msg.setWindowTitle("Ojemine")
                msg.setText("Du solltest vielleicht auch Würfel in den Becher packen!")
                msg.setIcon(QMessageBox.Information)

                x = msg.exec_()
                return
        self.wuerfelsound.play(loop=False)
        if self.Wurf == 1:
            for i in range(1, 6):
                exec("self.wuerfel{}.show()".format(i))

        for i in range(1, 6):
            exec("self.wuerfel{}.setEnabled(True)".format(i))
            exec("self.save{}.setEnabled(True)".format(i))

        while len(self.wuerfelbecher) < 5:
            self.wuerfelbecher.append(0)

        if self.Wurf == 1:
            gewuerfelt = self.Spielerliste[self.dran - 1].wuerfeln(5, 1)  # Wurf 1
            self.wuerfelbecher = gewuerfelt
            self.possiblePoints()

            self.Wurf = self.Wurf + 1
        elif self.Wurf == 2:

            gewuerfelt = self.Spielerliste[self.dran - 1].wuerfeln(len(self.wuerfelbecher), 2)  # Wurf 2
            for i in range(5):
                if self.wuerfelbecher[i] != 0:
                    self.wuerfelbecher[i] = gewuerfelt[i]
            self.Wurf = self.Wurf + 1
            self.possiblePoints()
        elif self.Wurf == 3:
            gewuerfelt = self.Spielerliste[self.dran - 1].wuerfeln(len(self.wuerfelbecher), 3)  # Wurf 3
            for i in range(5):
                if self.wuerfelbecher[i] != 0:
                    self.wuerfelbecher[i] = gewuerfelt[i]
            self.Wurf = self.Wurf + 1
            self.pushButtonwuerfeln.setEnabled(False)
            self.possiblePoints()

        for i in range(len(self.wuerfelbecher)):

            if gewuerfelt[i] == 1:
                exec("self.wuerfel{}.setIcon(QIcon('wuerfel1.png'))".format(i + 1))
            if gewuerfelt[i] == 2:
                exec("self.wuerfel{}.setIcon(QIcon('wuerfel2.png'))".format(i + 1))
            if gewuerfelt[i] == 3:
                exec("self.wuerfel{}.setIcon(QIcon('wuerfel3.png'))".format(i + 1))
            if gewuerfelt[i] == 4:
                exec("self.wuerfel{}.setIcon(QIcon('wuerfel4.png'))".format(i + 1))
            if gewuerfelt[i] == 5:
                exec("self.wuerfel{}.setIcon(QIcon('wuerfel5.png'))".format(i + 1))
            if gewuerfelt[i] == 6:
                exec("self.wuerfel{}.setIcon(QIcon('wuerfel6.png'))".format(i + 1))

    def wuerfelsave(self, saven):

        self.gesichert.append(self.wuerfelbecher[saven])
        längesave = len(self.gesichert)
        wert = self.wuerfelbecher[saven]
        exec("self.wuerfel{}.hide()".format(saven + 1))
        exec("self.save{}.setIcon(QIcon('wuerfel{}.png'))".format(längesave, wert))
        self.wuerfelbecher[saven] = 0
        for i in range(längesave):
            exec("self.save{}.setEnabled(True)".format(i + 1))
        for i in range(längesave, 5):
            exec("self.save{}.setEnabled(False)".format(i + 1))

    def wuerfelzurueck(self, back):

        längesave = len(self.gesichert)
        wert = self.gesichert[back]
        gefunden = 0
        for i in range(5):
            if self.wuerfelbecher[i] == 0:
                exec("self.wuerfel{}.show()".format(i + 1))
                exec("self.wuerfel{}.setIcon(QIcon('wuerfel{}.png'))".format(i + 1, wert))
                self.wuerfelbecher[i] = wert
                gefunden = 1
                break
        if gefunden == 0:
            self.wuerfelbecher.append(wert)
            exec("self.wuerfel{}.show()".format(len(self.wuerfelbecher + 1)))
            exec("self.wuerfel{}.setIcon(QIcon('wuerfel{}.png'))".format(len(self.wuerfelbecher + 1), wert))

        for j in range(längesave - back - 1):
            if back == 0:
                exec("self.save{}.setIcon(QIcon('wuerfel{}.png'))".format(j + back + 1, self.gesichert[back + j + 1]))
            # elif back == 0:
            # exec("self.save{}.setIcon(QIcon('wuerfel{}.png'))".format(j + back + 1, self.gesichert[back + j]))
            elif back != 0:
                exec("self.save{}.setIcon(QIcon('wuerfel{}.png'))".format(j + back + 1, self.gesichert[back + j + 1]))

        exec("self.save{}.setIcon(QIcon('save.png'))".format(längesave))
        self.gesichert.pop(back)
        exec("self.save{}.setEnabled(False)".format(längesave))

    def naechster(self):
        self.Spielerliste[self.dran - 1].getPunkte()

        for i in range(13, 19):
            labelnum = i - 12
            exec(
                "self.labelS{}_{}.setText(str(self.Spielerliste[self.dran-1].bisherig[{}]))".format(self.dran, labelnum,
                                                                                                    i))
        if self.dran < self.numplayers:

            self.dran = self.dran + 1
            self.Wurf = 1

            for i in range(13):
                self.buttonList[self.dran - 2][i].setEnabled(False)
                # self.listlist[self.dran - 1][i].setEnabled(True)
                if self.Spielerliste[self.dran - 1].bisherig[i] != ' ':
                    self.buttonList[self.dran - 1][i].setEnabled(False)
        else:
            self.dran = 1
            self.Wurf = 1
            self.Runde = self.Runde + 1
            for i in range(13):
                self.buttonList[self.numplayers - 1][i].setEnabled(False)
                # self.listlist[self.dran - 1][i].setEnabled(True)
                if self.Spielerliste[self.dran - 1].bisherig[i] != ' ':
                    self.buttonList[self.dran - 1][i].setEnabled(False)
        self.pushButtonwuerfeln.setEnabled(True)
        if self.Runde <= 13:
            self.popup()
        else:
            self.pushButtonrestart.setEnabled(True)
            self.gewinner()
        for i in range(len(self.gesichert)):
            exec("self.save{}.setIcon(QIcon('save.png'))".format(i + 1))
        for i in range(5):
            exec("self.wuerfel{}.show()".format(i + 1))
            exec("self.wuerfel{}.setIcon(QIcon('wuerfel6.png'))".format(i + 1))
        for i in range(1, 6):
            exec("self.wuerfel{}.setEnabled(False)".format(i))
            exec("self.save{}.setEnabled(False)".format(i))
        while len(self.gesichert) > 0:
            self.gesichert.pop(0)

    def popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Nächster Spieler")
        msg.setText("Als nächster ist " + self.namelist[self.dran - 1] + " an der Reihe!")
        msg.setIcon(QMessageBox.Information)

        x = msg.exec_()

    def possiblePoints(self):
        for i in range(13):
            if self.Spielerliste[self.dran - 1].bisherig[i] != ' ':
                self.buttonList[self.dran - 1][i].setEnabled(False)
        tempbisherig = self.Spielerliste[self.dran - 1].possiblepoints(self.gesichert, self.wuerfelbecher, self.Wurf)
        for i in range(13):
            self.buttonList[self.dran - 1][i].setText(str(tempbisherig[i]))

    def eintragen(self, action):
        betrag = int(self.buttonList[self.dran - 1][action].text())
        self.Spielerliste[self.dran - 1].eintragen(action, betrag)

        for i in range(13):
            self.buttonList[self.dran - 1][i].setText(str(self.Spielerliste[self.dran - 1].bisherig[i]))
            self.buttonList[self.dran - 1][i].setEnabled(False)
        self.naechster()

    def gewinner(self):
        max = 0
        for i in range(len(self.Spielerliste) - 1):
            if self.Spielerliste[i].bisherig[18] < self.Spielerliste[i + 1].bisherig[18]:
                max = i + 1
        self.winnersound.play()
        msg = QMessageBox()
        msg.setWindowTitle("Gewinner")
        msg.setText("Der Gewinner des Spiels ist: " + str(self.namelist[max]))
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
        self.bestenliste()

    def bestenliste(self):
        text = open("Bestenliste.txt")
        besten = text.readlines()
        text.close()
        Punkte = []
        Namen = []
        for i in range(10):
            getValues = besten[i].split()
            Namen.append(str(getValues[0]))
            Punkte.append(int(getValues[1]))
        for i in range(self.numplayers):
            for j in range(10):
                if self.Spielerliste[i].bisherig[18] >= Punkte[9-j] and j==9: #Spieler hat mehr Punkte als Spieler in Bestenliste
                    for k in range(j):  # Platz machen
                        besten[9 - k] = besten[9 - k - 1]
                    besten[0] = self.label_1.text() + " " + str(self.Spielerliste[i].bisherig[18])  # Einfügen
                    msg = QMessageBox()
                    msg.setWindowTitle("Bestenliste")
                    msg.setText("Die Bestenliste wurde aktualisiert! Schauen Sie mal nach")
                    msg.setIcon(QMessageBox.Information)
                    x = msg.exec_()
                elif self.Spielerliste[i].bisherig[18] < Punkte[9-j] and j == 0:
                    break
                elif self.Spielerliste[i].bisherig[18] >= Punkte[9-j]:
                    pass
                else: #sobald Wert nicht mehr größer muss an dieser Stelle eingeordnet werden
                    #9-j-1 um an Stelle dahinter einzusetzen
                    for k in range(j-1): #Platz machen
                        besten[9-k] = besten[9-k-1]
                    besten[9-j+1] = self.label_1.text() + " " +str(self.Spielerliste[i].bisherig[18]) + "\n" #Einfügen
                    msg = QMessageBox()
                    msg.setWindowTitle("Bestenliste")
                    msg.setText("Die Bestenliste wurde aktualisiert! Schauen Sie mal nach")
                    msg.setIcon(QMessageBox.Information)
                    x = msg.exec_()
                    break
        text = open("Bestenliste.txt", "w")
        fileneu = "".join(besten)
        text.write(fileneu)
        text.close()

app = QtWidgets.QApplication(sys.argv)
MainWindow1 = QtWidgets.QMainWindow()
MainWindow1.setFixedSize(1061, 652)
MainWindow2 = QtWidgets.QMainWindow()
MainWindow2.setFixedSize(1211, 842)
MainWindow3 = QtWidgets.QMainWindow()
MainWindow3.setFixedSize(778, 611)
MainWindow4 = QtWidgets.QMainWindow()
MainWindow4.setFixedSize(636, 370)

spiel = spielmenue(MainWindow2)
ui = hauptmenue(MainWindow1)
help = help(MainWindow3)
beste = bestenliste(MainWindow4)
MainWindow1.show()
app.exec_()
