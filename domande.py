"""
    permutazioni
    These methods are present in itertools package


Le permutazioni ci occorrono per presentare le risposte in ordine casuale
ad ogni domanda




"""

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