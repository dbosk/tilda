from bintree import Bintree

def main():
    alfabet="abcdefghijklmnopqrstuvwxyzåäö"
    rekord=""

    svenska=Bintree()
    svenskfil = open("words.txt")
    for rad in svenskfil.readlines():
        svenska.put(rad.strip())     #Ta bort returtecknet

    rekord = byggut("", alfabet, svenska)
    print("Längsta strykord: ", rekord)

def byggut(grundord, alfabet, ordlista):
    rekord = grundord
    for tecken in alfabet:
        nytt_ord = grundord + tecken
        if nytt_ord in ordlista:
            nytt_rekord = byggut(nytt_ord, alfabet, svenska)
            if len(nytt_rekord) > len(rekord):
                rekord = nytt_rekord
    return rekord

if __name__ == "__main__":
    main()
