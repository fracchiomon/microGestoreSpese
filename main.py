# This is a sample Python script.
import datetime
import os


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class Spesa:

    def __init__(self, nome, importo, data):
        self.nomeSpesa = nome
        self.importo = importo
        self.dataSpesa = data

    def toString(self):
        return str(self.nomeSpesa + "\t" + str(self.importo) + "€\t" + self.dataSpesa)

    def toStringCSV(self):
        return str(self.nomeSpesa + "," + str(self.importo) + "," + self.dataSpesa)


def clear():
    os.environ['TERM'] = 'xterm-256color'
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")
    return


def nuovaSpesa():
    nome = input("Nome Spesa:\t")
    spesa = float(input("Quanto hai speso?\t"))
    fattoOggi = int(input("Fatta oggi?\n1: Si\t2: No\nScelta:\t"))
    if fattoOggi == 1:
        data = datetime.date.today()
    else:
        mese = int(input("Mese:\t"))
        giorno = int(input("Giorno:\t"))
        data = datetime.date(datetime.date.today().year, mese, giorno)

    oggettoSpesa = Spesa(nome, spesa, datetime.date.isoformat(data))
    stackSpese.append(oggettoSpesa)
    return


def stampaTabella():
    for spesa in stackSpese:
        print(spesa.toString() + "\n")
    print("\n")
    return


def leggiTabella():
    try:
        fileSpese = open("gestoreSpese.csv", "rt")
        with fileSpese as fp:
            for stringa in fp:
                print(stringa)
        fileSpese.close()
    except FileNotFoundError:
        print("\n\n***IL FILE NON ESISTE.***\n\n\n")
    return


def scriviTabella():
    fileSpese = open("gestoreSpese.csv", "at")
    with fileSpese as fp:
        for spesa in stackSpese:
            fp.write(spesa.toStringCSV())
            fp.write("\n")
    fileSpese.close()
    return


def distruggiTutto():
    if os.path.exists("gestoreSpese.csv"):
        os.remove("gestoreSpese.csv")
        file = open("gestoreSpese.csv", "wt")
        file.write("Spesa,Importo,Data")
        file.write("\n")
        file.close()
    else:
        print("The file does not exist")


def menu():
    clear()
    print("Cosa facciamo?\n")
    print(
        "1:\tInserisci Spesa\n2:\tStampa Tabella\n3:\tScrivi in DB\n4:\tLeggi Tabella\n5:\tEsci\n\n0:\tDISTRUGGI "
        "TABELLA\n")
    scelta = int(input("Scelta: "))
    if scelta == 1:
        nuovaSpesa()
    elif scelta == 2:
        stampaTabella()
    elif scelta == 3:
        scriviTabella()
    elif scelta == 4:
        leggiTabella()
    elif scelta == 5:
        exit(0)
    elif scelta == 0:
        conferma = input("Amo sei sicuro di cancellare tutto? (Y/N)\t")
        if conferma == "Y" or conferma == "y":
            distruggiTutto()
        else:
            menu()
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # pila di oggetti Spesa da inserire poi in tabella
    stackSpese = []
    while 1:
        menu()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/