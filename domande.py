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
        n= randint(0, self._NUMERO_COMB - 1)

        uscita = f"Livello {self.difficolta}) {self.testoDomanda}\n"
        i=1
        for k in self.lst_perm[n]:
            uscita = uscita + str(i) +'. ' + self.risposte[k] +'\n'
            i += 1
        uscita = uscita + "\n\n"

        return uscita


d1 = Domanda("Lingua ufficiale del Brasile?", 0, ['Portoghese', 'Spagnolo', 'Urdu', 'Klingon'])

print(d1.dispDomanda())