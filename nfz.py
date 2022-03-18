import pickle
from classes import *

class Program(NFZController):

    def __init__(self):
        super().__init__()
        try:
            plik = open("nfz.dat", "rb")
            self.lista_przychodni = pickle.load(plik)
            plik.close()
        except:
            plik = open("nfz.dat", "wb")
            pickle.dump([], plik)
            plik.close()
        self.menu()

    def menu(self):

        while (True):
            try:
                menu = int(input("1 - Przychodnia, 2 - Pacjent, 3 - Statystyki, 4 - Koniec "))
                print()

                if menu == 1:
                    menu1 = int(input("1 - Dodaj przychodnię, 2 - Usuń przychodnię, 3 - Dodaj pacjenta do przychodni, \n"
                                         "4 - Usuń pacjenta z przychodni, 5 - Lista przychodni, 6 - Lista pacjentów w przychodni "))
                    print()
                    if menu1 == 1:
                        nazwa = input("    Podaj nazwę przychodni: ")
                        miasto = input("    Podaj miasto przychodni: ")
                        print()
                        self.dodaj_przychodnie(nazwa, miasto)

                    elif menu1 == 2:
                        nazwa = input("    Podaj nazwę przychodni: ")
                        if self.szukaj_przychodnie(nazwa) == True:
                            self.usun_przychodnie(nazwa)
                        else:
                            print("    Nie znaleziono przychodni.\n")
                    elif menu1 == 3:
                        nazwa_przychodni = input("    Podaj nazwę przychodni: ")
                        if self.szukaj_przychodnie(nazwa_przychodni) == True:
                            imie = input("    Podaj imię pacjenta: ")
                            nazwisko = input("    Podaj nazwisko pacjenta: ")
                            self.dodaj_pacjenta(nazwa_przychodni, imie, nazwisko)
                        else:
                            print("    Nie znaleziono przychodni.\n")

                    elif menu1 == 4:
                        nazwa_przychodni = input("    Podaj nazwę przychodni: ")
                        if self.szukaj_przychodnie(nazwa_przychodni) == True:
                            nazwisko = input("    Podaj nazwisko pacjenta: ")
                            self.usun_pacjenta(nazwa_przychodni, nazwisko)
                        else:
                            print("    Nie znaleziono przychodni.\n")

                    elif menu1 == 5:
                        self.pokaz_przychodnie()

                    elif menu1 == 6:
                        nazwa_przychodni = input("    Podaj nazwę przychodni: ")
                        if self.szukaj_przychodnie(nazwa_przychodni) == True:
                            self.pokaz_pacjentow(nazwa_przychodni)
                        else:
                            print("    Nie znaleziono przychodni.\n")

                    else:
                        print("    Nierozpoznana opcja menu.\n")

                elif menu == 2:
                    menu1 = int(input("1 - Dodaj chorobę pacjentowi, 2 - Lista chorób pacjenta, \n"
                                      "3 - Przepisz pacjenta do drugiej przychodni, 4 - Szukaj pacjenta "))
                    print()
                    if menu1 == 1:
                        nazwisko = input("    Podaj nazwisko pacjenta: ")
                        if self.szukaj_pacjenta(nazwisko) == True:
                            choroba = input("    Podaj chorobę pacjenta: ")
                            self.dodaj_chorobe(nazwisko, choroba)
                        else:
                            print("    Nie znaleziono pacjenta.\n")

                    elif menu1 == 2:
                        nazwisko = input("    Podaj nazwisko pacjenta: ")
                        if self.szukaj_pacjenta(nazwisko) == True:
                            self.pokaz_choroby(nazwisko)
                        else:
                            print("    Nie znaleziono pacjenta.\n")

                    elif menu1 == 3:
                        nazwisko = input("    Podaj nazwisko pacjenta: ")
                        if self.szukaj_pacjenta(nazwisko) == True:
                            nazwa_przychodni = input("    Podaj nazwę nowej przychodni pacjenta: ")
                            if self.szukaj_przychodnie(nazwa_przychodni) == True:
                                print(self.przepisz_pacjenta(nazwisko, nazwa_przychodni))
                            else:
                                print("    Nie znaleziono przychodni.\n")
                        else:
                            print("    Nie znaleziono pacjenta.\n")

                    elif menu1 == 4:
                        nazwisko = input("    Podaj nazwisko pacjenta: ")
                        print()
                        if self.szukaj_pacjenta(nazwisko) == True:
                            self.pokaz_pacjenta(nazwisko)
                        else:
                            print("    Nie znaleziono pacjenta.\n")

                    else:
                        print("    Nierozpoznana opcja menu.\n")

                elif menu == 3:
                    menu1 = int(input("1 - Ilość pacjentów w przychodni, 2 - Zestawienie ilościowe chorób "))
                    print()
                    if menu1 == 1:
                        nazwa_przychodni = input("    Podaj nazwę przychodni: ")
                        if self.szukaj_przychodnie(nazwa_przychodni) == True:
                            self.ilosc_pacjentow(nazwa_przychodni)
                        else:
                            print("    Nie znaleziono przychodni.\n")

                    elif menu1 == 2:
                        self.statystyka_chorob()
                    else:
                        print("    Nierozpoznana opcja menu.\n")

                elif menu == 4:
                    self.zapisz_do_pliku()
                    print("    KONIEC PROGRAMU.")
                    break

                else:
                    print("    Nierozpoznana opcja menu.\n")

            except ValueError:
                print("\n    Nierozpoznana opcja menu.\n")

obiekt = Program()