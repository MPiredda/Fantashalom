import openpyxl

def filter(data):
    lista = []

    for item in data:
            lista.append(f"{item['Nome']} {item['Qt.A']}")
    return lista

def format_data(data):
    array_P = []
    array_D = []
    array_C = []
    array_A = []

    if 'P' in data:
        for item in data['P']:
            name, value = item
            array_P.append({'Nome': name, 'Qt.A': value})

    if 'D' in data:
        for item in data['D']:
            name, value = item
            array_D.append({'Nome': name, 'Qt.A': value})

    if 'C' in data:
        for item in data['C']:
            name, value = item
            array_C.append({'Nome': name, 'Qt.A': value})

    if 'A' in data:
        for item in data['A']:
            name, value = item
            array_A.append({'Nome': name, 'Qt.A': value})

    P= filter(array_P)
    D= filter(array_D)
    C= filter(array_C)
    A= filter(array_A)
    return P, D, C, A

def leggi_colonna_quarta_sesta_insieme(file_path):
    try:
        # Carica il file XLSX
        workbook = openpyxl.load_workbook(file_path)
        # Seleziona il primo foglio di lavoro
        sheet = workbook.active
        # Inizializza un dizionario per contenere le coppie di valori (colonna 4, colonna 6)
        valori_colonna_4_6 = {}
        # Itera attraverso le righe e aggiunge i valori delle colonne 4 e 6 al dizionario
        for row in sheet.iter_rows(min_row=1, min_col=2, max_col=6, values_only=True):
            valore_colonna_2 = row[0]
            valore_colonna_4 = row[2]
            valore_colonna_6 = row[4]

            # Se il valore della colonna 2 non è già presente nel dizionario, lo aggiunge
            if valore_colonna_2 not in valori_colonna_4_6:
                valori_colonna_4_6[valore_colonna_2] = [(valore_colonna_4, valore_colonna_6)]
            else:
                valori_colonna_4_6[valore_colonna_2].append((valore_colonna_4, valore_colonna_6))

        # Restituisci il dizionario contenente le coppie di valori (colonna 4, colonna 6)
        return valori_colonna_4_6

    except Exception as e:
        print("Si è verificato un errore durante la lettura del file:", e)
        return None

# Esempio di utilizzo
file_path = "Quote.xlsx"
valori_colonna_4_6 = leggi_colonna_quarta_sesta_insieme(file_path)
P, D, C, A = format_data(valori_colonna_4_6)

def utilizzo(file_path):
    valori_colonna_4_6 = leggi_colonna_quarta_sesta_insieme(file_path)
    P, D, C, A = format_data(valori_colonna_4_6)
    return P,D,C,A









