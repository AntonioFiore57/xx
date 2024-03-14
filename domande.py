"""
    permutazioni
    These methods are present in itertools package


Le permutazioni ci occorrono per presentare le risposte in ordine casuale
ad ogni domanda


# A Python program to print all
# permutations using library function
from itertools import permutations

# Get all permutations of [1, 2, 3, 4]
perm = permutations([1, 2, 3, 4])

# Print the obtained permutations
lst_perm = list(perm)

print(len(lst_perm))

for i in lst_perm:
    print(i)


"""

from itertools import permutations
from random import randint

class Domanda:
    def __init__(self, testoDomanda, difficolta, risposte):
        self.testoDomanda = testoDomanda
        self.difficolta = difficolta
        # risposte è una lista. Il primo elemento della lista è la risposta corretta
        self.risposte = risposte

        self.perm = permutations([0, 1, 2, 3])
        self.lst_perm = list(self.perm)
        self._NUMERO_COMB = len(self.lst_perm)
        self._index_permutazione_risposte = randint(0, self._NUMERO_COMB - 1)
        self.rispostaCorretta = self.lst_perm[self._index_permutazione_risposte].index(0)
    def dispDomanda(self):
        '''
        schema visualizzazione
                Livello 0) Lingua ufficiale del Brasile?
                1. Spagnolo
                2. Francese
                3. Portoghese
                4. Inglese

        :return:
        '''
        # generiamo un casuale intero tra 0 e self._NUMERO_COMB per scegliere la permutazione
        # dell'ordine delle domande
        n= self._index_permutazione_risposte

        uscita = f"Livello {self.difficolta}) {self.testoDomanda}\n"
        i=1
        for k in self.lst_perm[n]:
            uscita = uscita + str(i) +'. ' + self.risposte[k] +'\n'
            i += 1
        return uscita
    def checkRisposta(self, n):
        if n not in (1,2,3,4):
            raise ValueError("Valore non consentito")
        if self.rispostaCorretta == n - 1:
            # risposta esatta
            return True
        else:
            return False

"""
d1 = Domanda("Lingua ufficiale del Brasile?", 0, ['Portoghese', 'Spagnolo', 'Urdu', 'Klingon'])

print(d1.dispDomanda())
risposta = int(input("Inserisci la risposta: "))
if d1.checkRisposta(risposta):
    print("Risposta corretta!")
else:
    print(f"Risposta sbagliata! La risposta corretta era: {d1.rispostaCorretta +1}")
"""

# Dal contenuto del file domande.txt si ricava un dizionario in cui le chiavi sono il livello
# di difficoltà delle domande e il valore una lista delle domande con quel grado di difficoltà.
#
#
f = open("F:\\U3E\\TdP_Corno\\TdP2024\\Lab_01\\domande.txt", 'r', encoding='utf-8')
righe = [y for y in [x.strip() for x in f.readlines()] if y!='' ]
f.close()
dict_domande = {}


for i in range(len(righe)//6):
    d = Domanda(righe[i*6], righe[i*6+1], [righe[i*6+2], righe[i*6+3], righe[i*6+4], righe[i*6+5]   ])
    if int(righe[i*6+1]) not in dict_domande:
        dict_domande[int(righe[i*6+1])] = list()
        dict_domande[int(righe[i * 6 + 1])].append(d)
    else:
        dict_domande[int(righe[i * 6 + 1])].append(d)


# I punti dei giocatori vengono gestiti con una lista di tuple
# [ (nikname1, punti), (nikname2, punti) .... ]
players = list()
f = open("F:\\U3E\\TdP_Corno\\TdP2024\\Lab_01\\punti.txt", 'r', encoding='utf-8')
righe = [x.strip() for x in f.readlines()]
f.close()

for riga in righe:
    nikname = riga.split()
    players.append( (nikname[0], int(nikname[1])  ) )

MAX_LIVELLO = max(dict_domande.keys())

# non ci preoccupiamo se un nikname è già presente
# Visualizzare una breve spiegazione delle regole del gioco

nikname = input("Inserisci il tuo nikname: ")

gioco = True
punti = 0
livello = 0
while gioco:
    numeroDomandeLivello = len(dict_domande[livello])
    d = dict_domande[livello][randint(0, numeroDomandeLivello-1)]
    print(d.dispDomanda())

    risposta = int(input("Inserisci la risposta: "))
    if d.checkRisposta(risposta):
        print("Risposta corretta!")
        livello += 1
        if livello>MAX_LIVELLO:
            gioco = False
    else:
        print(f"Risposta sbagliata! La risposta corretta era: {d.rispostaCorretta + 1}")
        gioco=False
    print()


