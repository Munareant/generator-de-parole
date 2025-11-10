import string
import random

def generator_de_parole(lungime):
    """Genereaza o parola aleatorie cu lungime specifica"""
    caractere = string.ascii_letters + string.digits + string.punctuation
    parola = ''.join(random.choice(caractere) for _ in range(lungime))
    return parola
if __name__=="__main__":
    print("--- Generator simplu de parole")

    try:
        lungime_parola = int(input("Introdu lungimea dorita pentru parola"))
        if lungime_parola <= 0:
            print("Te rog introdu un numar pozitiv.")
        else:
            parola_noua = generator_de_parole(lungime_parola)
            print(f"\nParola ta generata este:{parola_noua}")
    except ValueError:
        print("Eroare: Te rog introdu un numar valid")