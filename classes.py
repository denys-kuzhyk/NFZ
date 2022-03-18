import pickle

class Pacjent:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.lista_chorob = []

class Przychodnia:

    def __init__(self, nazwa, miasto):
        self.lista_pacjentow = []
        self.nazwa = nazwa
        self.miasto = miasto

class NFZController:

    def __init__(self):
        self.lista_przychodni = []

    def zapisz_do_pliku(self):
        plik = open("nfz.dat", "wb")
        pickle.dump(self.lista_przychodni, plik)
        plik.close()

    def dodaj_przychodnie(self, nazwa, miasto):
        ob = Przychodnia(nazwa, miasto)
        self.lista_przychodni.append(ob)
        self.zapisz_do_pliku()
        print("    Dodano przychodnię do listy.\n")

    def usun_przychodnie(self, nazwa):
        for i in self.lista_przychodni:
            if i.nazwa == nazwa:
                self.lista_przychodni.remove(i)
                self.zapisz_do_pliku()
                print("    Pomyślnie usunięto przychodnię.\n")

    def dodaj_pacjenta(self, nazwa_przychodni, imie, nazwisko):
        for i in self.lista_przychodni:
            if i.nazwa == nazwa_przychodni:
                ob = Pacjent(imie, nazwisko)
                i.lista_pacjentow.append(ob)
                self.zapisz_do_pliku()
                print("    Pomyślnie dodano pacjenta.\n")

    def usun_pacjenta(self, nazwa_przychodni, nazwisko):
        for i in self.lista_przychodni:
            if i.nazwa == nazwa_przychodni:
                for k in i.lista_pacjentow:
                    if k.nazwisko == nazwisko:
                        i.lista_pacjentow.remove(k)
                        self.zapisz_do_pliku()
                        print("    Pomyślnie usunięto pacjenta.\n")

    def pokaz_przychodnie(self):
        if len(self.lista_przychodni) == 0:
            print("    Lista jest pusta.\n")
        else:
            plik = open("nfz.dat", "rb")
            self.lista_przychodni = pickle.load(plik)
            plik.close()
            for i in self.lista_przychodni:
                print(f"    Przychodnia: {i.nazwa}, {i.miasto}")
            print()

    def pokaz_pacjentow(self, nazwa_przychodni):
        plik = open("nfz.dat", "rb")
        self.lista_przychodni = pickle.load(plik)
        plik.close()
        for i in self.lista_przychodni:
            if i.nazwa == nazwa_przychodni:
                if len(i.lista_pacjentow) > 0:
                    print()
                    for k in i.lista_pacjentow:
                        print(f"    Imię: {k.imie}\n    Nazwisko: {k.nazwisko}")
                        if len(k.lista_chorob) > 0:
                            for j in k.lista_chorob:
                                print("    Choroba: ", end="")
                                print(j)
                        else:
                            print("    Brak chorób.")
                        print("    -----------------\n")
                else:
                    print("    Lista pacjentów jest pusta.\n")

    def dodaj_chorobe(self, nazwisko, choroba):
        for i in self.lista_przychodni:
            for k in i.lista_pacjentow:
                if k.nazwisko == nazwisko:
                    znaleziono = False
                    for j in k.lista_chorob:
                        if j == choroba:
                            znaleziono = True
                    if znaleziono == False:
                        k.lista_chorob.append(choroba)
                        self.zapisz_do_pliku()
                        print("    Pomyślnie dodano chorobę.\n")
                    else:
                        print("    Ta choroba już jest w liście.\n")

    def pokaz_choroby(self, nazwisko):
        plik = open("nfz.dat", "rb")
        self.lista_przychodni = pickle.load(plik)
        plik.close()
        for i in self.lista_przychodni:
            for k in i.lista_pacjentow:
                if k.nazwisko == nazwisko:
                    if len(k.lista_chorob) > 0:
                        for j in k.lista_chorob:
                            print("    Choroba: ", end="")
                            print(j)
                        print()
                    else:
                        print("    Lista chorób pacjenta jest pusta.\n")

    def szukaj_przychodnie(self, nazwa):
        znaleziono = False
        for i in self.lista_przychodni:
            if i.nazwa == nazwa:
                znaleziono = True
                break

        return znaleziono

    def szukaj_pacjenta(self, nazwisko):
        znaleziono = False
        for i in self.lista_przychodni:
            for k in i.lista_pacjentow:
                if k.nazwisko == nazwisko:
                    znaleziono = True
                    break

        return znaleziono

    def przepisz_pacjenta(self, nazwisko, przychodnia):

        for i in self.lista_przychodni:
            for k in i.lista_pacjentow:
                if k.nazwisko == nazwisko:
                    i.lista_pacjentow.remove(k)
                    for j in self.lista_przychodni:
                        if j.nazwa == przychodnia:
                            j.lista_pacjentow.append(k)
                            self.zapisz_do_pliku()
                            return f"    Przepisano pacjenta do {przychodnia}\n"

    def pokaz_pacjenta(self, nazwisko):

        for i in self.lista_przychodni:
            for k in i.lista_pacjentow:
                if k.nazwisko == nazwisko:
                    print("    Pacjent:")
                    print(f"    Imię: {k.imie}, Nazwisko: {k.nazwisko}, Przychodnia: {i.nazwa}\n")

    def ilosc_pacjentow(self, nazwa_przychodni):

        for i in self.lista_przychodni:
            if i.nazwa == nazwa_przychodni:
                if len(i.lista_pacjentow) > 0:
                    print(f"    Przychodnia: {i.nazwa}, Ilość pacjentów: {len(i.lista_pacjentow)}\n")
                else:
                    print("    Lista pacjentów w tej przychodni jest pusta.\n")

    def statystyka_chorob(self):
        choroby = set()
        for i in self.lista_przychodni:
            for k in i.lista_pacjentow:
                for j in k.lista_chorob:
                    choroby.add(j)
        library = {}
        for i in choroby:
            ilosc = 0
            for j in self.lista_przychodni:
                for k in j.lista_pacjentow:
                    for l in k.lista_chorob:
                        if l == i:
                            ilosc += 1
            library[i] = ilosc
        if len(library) > 0:
            for i in library:
                print(f"    Choroba: {i}, częstość występowania: {library[i]}")
        else:
            print("    Lista chorób jest pusta.")
        print()
