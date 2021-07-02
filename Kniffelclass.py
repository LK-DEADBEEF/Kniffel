import random
#Die Main muss fragen wie viele Leute mitspielen wollen, für jeden Spieler muss eine Klasse angelegt werden.
#Nacheinander muss gewürfelt werden und abgefragt werden, was gespeichert werden soll und nach 3 Würfen einen Score eintragen
#und das Wurfrecht an den nächsten Spieler übergeben. Reihenfolge wichtig - Am Anfang benennen wer am Zug ist
class Kniffel:
    def __init__ (self): #Der Spieler braucht noch eine eigene Punkteliste (muss noch eingefügt werden)
        self.punkte=0
        self.name = ''
        self.bisherig=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] #Das wird später die Ergebnisliste

    def wuerfeln(self,numwuerfel,wurf):
        gewuerfeltewuerfel = []
        if numwuerfel > 0:
            for i in range (numwuerfel):
                gewuerfeltewuerfel.append(random.randint(1, 6))
                #print(gewürfeltewuerfel)
            
            return gewuerfeltewuerfel
        else:
            print("Sie haben keine Würfel im Becher, die sie Würfeln können")
        return gewuerfeltewuerfel,wurf
    
    def save(self,wuerfel,save,wurf):
        if wurf < 3:
            ende = 'n'
            while ende != 'J':
                nochmal = 'j'
                while nochmal == 'j':
                    pos=int(input("Welche Würfel/Position möchten Sie für den nächsten Zug sichern?: "+ str(wuerfel))) #Abfangen falls keiner gespeichert werden soll
                    
                    save.append(wuerfel[pos]) #Abfangen falls doch nichts verändert werden soll
                    wuerfel.pop(pos)
                    nochmal = input("Möchten sie nochmal etwas speichern? j/n"+str(wuerfel)+str(save))
                zurueck = (input("Eine Position doch lieber würfeln? j/n"+str(wuerfel)+str(save)))
                while zurueck == 'j':
                    wen = int(input("Welche Position soll lieber gewürfelt werden?"+str(wuerfel)+str(save)))
                    wuerfel.append(save[wen])
                    save.pop(wen)
                    zurueck = input("Nochmal etwas von den gesicherten Würfeln verschieben? j/n")
                ende = input("Sind Sie mit Ihrer Eingabe zufrieden? J/N")

            return wuerfel,save
        else: 
            for k in range (len(wuerfel)):
                save.append(wuerfel[k])
            return wuerfel,save

    def possiblepoints(self,save,wuerfel,wurf):
        tempsave = []
        for i in range (len(save)):
            tempsave.append(save[i])
        for i in range (len(wuerfel)):
                tempsave.append(wuerfel[i])
        tempbisherig = []
        for i in range (len(self.bisherig)):
            tempbisherig.append(self.bisherig[i])

        
        einser = 0 #Wie viele Einser?
        for i in range (len(tempsave)):
            if tempsave[i] == 1:
                einser = einser + tempsave[i]
        if tempbisherig[0] == ' ': #Prüfen ob schon eingetragen wurde.        
            tempbisherig[0] = einser
        
        
        zweier = 0 #Wie viele Zweier?
        for j in range (len(tempsave)):
            if tempsave[j] == 2:
                zweier = zweier + 1 
        if tempbisherig[1] == ' ': #Prüfen ob schon eingetragen wurde.
            tempbisherig[1] = zweier * 2

        
        dreier = 0 #Wie viele Zweier?
        for k in range (len(tempsave)):
            if tempsave[k] == 3:
                dreier = dreier + 1
        if tempbisherig[2] == ' ': #Prüfen ob schon eingetragen wurde.                
            tempbisherig[2] = dreier * 3

        
        vierer = 0 #Wie viele Zweier?
        for l in range (len(tempsave)):
            if tempsave[l] == 4:
                vierer = vierer + 1
        if tempbisherig[3] == ' ': #Prüfen ob schon eingetragen wurde.                
            tempbisherig[3] = vierer * 4

        
        fuenfer = 0 #Wie viele Zweier?
        for m in range (len(tempsave)):
            if tempsave[m] == 5:
                fuenfer = fuenfer + 1
        if tempbisherig[4] == ' ': #Prüfen ob schon eingetragen wurde.                
            tempbisherig[4] = fuenfer * 5

        
        sechser = 0 #Wie viele Zweier?
        for k in range(len(tempsave)):
            if tempsave[k] == 6:
                sechser = sechser + 1
        if tempbisherig[5] == ' ': #Prüfen ob schon eingetragen wurde.                
            tempbisherig[5] = sechser * 6
        
        #Unterer Teil
        #Dreierpasch
        if tempbisherig[6] == ' ': #Prüfen ob schon eingetragen wurde.
            if einser >= 3 or zweier >= 3 or dreier >= 3 or vierer >= 3 or fuenfer >= 3 or sechser >= 3:
                dpasch = 0
                for i in range (len(tempsave)):
                    dpasch = tempsave[i] + dpasch
                tempbisherig[6] = dpasch
            else:
                tempbisherig[6] = 0

        #Viererpasch:
        if tempbisherig[7] == ' ': #Prüfen ob schon eingetragen wurde.
            if einser >= 4 or zweier >= 4 or dreier >= 4 or vierer >= 4 or fuenfer >= 4 or sechser >= 4:
                vpasch = 0
                for i in range(len(tempsave)):
                    vpasch = tempsave[i] + vpasch
                tempbisherig[7] = vpasch
            else:
                tempbisherig[7] = 0

        #Full House:

        if tempbisherig[8] == ' ': #Prüfen ob schon eingetragen wurde.
            if einser == 3 or zweier == 3 or dreier == 3 or vierer == 3 or fuenfer == 3 or sechser == 3: #Prüfen ob Drilling vorhanden?
                if einser == 2 or zweier == 2 or dreier == 2 or vierer == 2 or fuenfer == 2 or sechser == 2: #Prüfen ob Paar vorhanden
                    tempbisherig[8] = 25
            else: 
                tempbisherig[8] = 0
        
        #kleine Straße

        if tempbisherig[9] == ' ': #Prüfen ob schon eingetragen wurde.
            if einser >= 1 and zweier >= 1 and dreier >= 1 and vierer >= 1:
                tempbisherig[9] = 30
            elif zweier >= 1 and dreier >= 1 and vierer >= 1 and fuenfer >= 1:
                tempbisherig[9] = 30
            elif dreier >= 1 and vierer >= 1 and fuenfer >= 1 and sechser >= 1:
                tempbisherig[9] = 30
            else: 
                tempbisherig[9] = 0
            
        #große Straße

        if tempbisherig[10] == ' ': #Prüfen ob schon eingetragen wurde.
            if einser >= 1 and zweier >= 1 and dreier >= 1 and vierer >= 1 and fuenfer >= 1:
                tempbisherig[10] = 40
            elif zweier >= 1 and dreier >= 1 and vierer >= 1 and fuenfer >= 1 and sechser >= 1:
                tempbisherig[10] = 40
            else:
                tempbisherig[10] = 0

        #Kniffel
        if tempbisherig[11] == ' ': #Prüfen ob schon eingetragen wurde.
            if einser == 5 or zweier == 5 or dreier == 5 or vierer == 5 or fuenfer == 5 or sechser == 5: #Prüfen ob Kniffel vorhanden?        
                tempbisherig[11] = 50
            else:
                tempbisherig[11] = 0
        elif tempbisherig[11] == 50 and einser == 5 and tempbisherig[0] == ' ': #2. Kniffel nur eintragbar wenn Feld oben frei
            tempbisherig[0] = 55
        elif tempbisherig[11] == 50 and zweier == 5 and tempbisherig[1] == ' ':
            tempbisherig[1] = 60
        elif tempbisherig[11] == 50 and dreier == 5 and tempbisherig[2] == ' ':
            tempbisherig[2] = 65
        elif tempbisherig[11] == 50 and vierer == 5 and tempbisherig[3] == ' ':
            tempbisherig[3] = 70
        elif tempbisherig[11] == 50 and fuenfer == 5 and tempbisherig[4] == ' ':
            tempbisherig[4] = 75
        elif tempbisherig[11] == 50 and sechser == 5 and tempbisherig[5] == ' ':
            tempbisherig[5] = 80

        # Chance
        if tempbisherig[12] == ' ': #Prüfen ob schon eingetragen wurde.
            sum = 0
            for i in range (len(tempsave)):
                sum = sum + tempsave[i]
            tempbisherig[12] = sum

        return tempbisherig
            

    def getPunkte(self):
        punkteoben = 0
        punkteunten = 0
        for i in range (6): #Punkte oberer Teil
            if self.bisherig[i] == ' ':
                pass
            else:
                punkteoben = self.bisherig[i] + punkteoben
        if punkteoben >= 63: #extrapunkte bei mehr als 63 Punkten im oberen Teil
            self.bisherig[13] = punkteoben
            self.bisherig[14] = 35
            self.bisherig[15] = punkteoben + 35 #Gesamtoben
        
        else:
            self.bisherig[13] = punkteoben
            self.bisherig[14] = 0
            self.bisherig[15] = punkteoben #Gesamtoben
        
        for i in range (6,13): #Punkte unterer Teil
            if self.bisherig[i] == ' ':
                pass
            else:
                punkteunten = self.bisherig[i] + punkteunten
        self.bisherig[16] = punkteunten
        self.bisherig[17] = punkteoben
        self.bisherig[18] = self.bisherig[16] + self.bisherig[15] #GesPunkte sind Punkteoben + Punkteunten

    def eintragen(self,stelle,punkte):
        self.bisherig[stelle] = punkte
        #print(self.bisherig)