import random
import re


def shuffle_array(array):
    # Shuffle the array in place and return the shuffled array
    random.shuffle(array)
    return array


def leggi_file_e_struttura(file_path):
    portieri = []
    difensori = []
    centrocampisti = []
    attaccanti = []

    with open(file_path, 'r') as file:
        current_section = None
        for line in file:
            line = line.strip()
            if line == "PORTIERI":
                current_section = portieri
            elif line == "DIFENSORI":
                current_section = difensori
            elif line == "CENTROCAMPISTI":
                current_section = centrocampisti
            elif line == "ATTACCANTI":
                current_section = attaccanti
            else:
                current_section.append(line)

    portieri = rimuovi_parentesi(portieri)
    difensori = rimuovi_parentesi(difensori)
    centrocampisti= rimuovi_parentesi(centrocampisti)
    attaccanti = rimuovi_parentesi(attaccanti)

    return portieri, difensori, centrocampisti, attaccanti

def rimuovi_parentesi(array):
    risultato = []
    for elemento in array:
        nuovo_elemento = re.sub(r'\([^)]*\)', '', elemento)
        risultato.append(nuovo_elemento.strip())
    return risultato



# Esempio di utilizzo:
file_path = "lista.txt"
portieri, difensori, centrocampisti, attaccanti = leggi_file_e_struttura(file_path)



