import pickle

class Pacjent:  # we create a patient object out of this class

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.lista_chorob = []

class Przychodnia:  # this class creates a hospital object

    def __init__(self, nazwa, miasto):
        self.lista_pacjentow = []
        self.nazwa = nazwa
        self.miasto = miasto

class NFZController:  # probably the main class in the project, it performs
                      # different kinds of operations on hospitals and patients

    def __init__(self):
        self.lista_przychodni = []

    def zapisz_do_pliku(self):  # this function saves the data to the dat file
        plik = open("nfz.dat", "wb")
        pickle.dump(self.lista_przychodni, plik)
        plik.close()

    def dodaj_przychodnie(self, nazwa, miasto):  # this function creates a hospital
        ob = Przychodnia(nazwa, miasto)
        self.lista_przychodni.append(ob)
        self.zapisz_do_pliku()
        print("    Dodano przychodnię do listy.\n")

    def usun_przychodnie(self, nazwa):  # this function removes a hospital
        for i in self.lista_przychodni:    # checking if this hospital exists
            if i.nazwa == nazwa:    # it does exist, so we remove it from the list
                self.lista_przychodni.remove(i)
                self.zapisz_do_pliku()
                print("    Pomyślnie usunięto przychodnię.\n")

    def dodaj_pacjenta(self, nazwa_przychodni, imie, nazwisko):  # this function creates a patient
        for i in self.lista_przychodni:
            if i.nazwa == nazwa_przychodni:
                ob = Pacjent(imie, nazwisko)
                i.lista_pacjentow.append(ob)
                self.zapisz_do_pliku()
                print("    Pomyślnie dodano pacjenta.\n")

    def usun_pacjenta(self, nazwa_przychodni, nazwisko):  # this function removes a patient
        for i in self.lista_przychodni:    # checking if the hospital and the patient exist
            if i.nazwa == nazwa_przychodni:    # the hospital does exist
                for k in i.lista_pacjentow:
                    if k.nazwisko == nazwisko:  # the patient does exist so we remove them from the hospital
                        i.lista_pacjentow.remove(k)
                        self.zapisz_do_pliku()
                        print("    Pomyślnie usunięto pacjenta.\n")

    def pokaz_przychodnie(self):  # this function shows all the hospitals in the system
        if len(self.lista_przychodni) == 0:
            print("    Lista jest pusta.\n")
        else:   # if the hospital list is not empty, we load this list to a variable from
                # the dat file and then loop through each element to output the name and the city of a hospital
            plik = open("nfz.dat", "rb")
            self.lista_przychodni = pickle.load(plik)
            plik.close()
            for i in self.lista_przychodni:
                print(f"    Przychodnia: {i.nazwa}, {i.miasto}")
            print()

    def pokaz_pacjentow(self, nazwa_przychodni):  # this function displays all the patients in a particular hospital
        plik = open("nfz.dat", "rb")    # we get the list of hospitals to check if one exists
        self.lista_przychodni = pickle.load(plik)
        plik.close()
        for i in self.lista_przychodni:    # looping through the list to find the hospital
            if i.nazwa == nazwa_przychodni:    # once we found it, we check if there are any patients
                if len(i.lista_pacjentow) > 0:    # there are more than 0 patients, which is sad :(
                    print()
                    for k in i.lista_pacjentow:    # then we loop through each patient ad output their data
                        print(f"    Imię: {k.imie}\n    Nazwisko: {k.nazwisko}")
                        if len(k.lista_chorob) > 0:    # if the patient has any diseases, they will also be displayed
                            for j in k.lista_chorob:
                                print("    Choroba: ", end="")
                                print(j)
                        else:    # if they dont, we don't have to worry about that
                            print("    Brak chorób.")
                        print("    -----------------\n")
                else:    # if there are no patients in the hospital, we just print out following message
                    print("    Lista pacjentów jest pusta.\n")

    def dodaj_chorobe(self, nazwisko, choroba):  # this function adds a disease to a patient
        for i in self.lista_przychodni:     # looking for the patient
            for k in i.lista_pacjentow:
                if k.nazwisko == nazwisko:    # once we found them, we try to add the disease
                    znaleziono = False
                    for j in k.lista_chorob:    # checking if the disease isn't already in the list
                        if j == choroba:
                            znaleziono = True
                    if znaleziono == False:    # if it isn't - we add it to the list
                        k.lista_chorob.append(choroba)
                        self.zapisz_do_pliku()
                        print("    Pomyślnie dodano chorobę.\n")
                    else:    # if it is - we print out the message
                        print("    Ta choroba już jest w liście.\n")

    def pokaz_choroby(self, nazwisko):  # this function displays all of the patient's diseases
        plik = open("nfz.dat", "rb")    # loading the list of hospitals
        self.lista_przychodni = pickle.load(plik)
        plik.close()
        for i in self.lista_przychodni:    # looking for the patient
            for k in i.lista_pacjentow:
                if k.nazwisko == nazwisko:    # once we find them - loop through every disease and print it
                    if len(k.lista_chorob) > 0:
                        for j in k.lista_chorob:
                            print("    Choroba: ", end="")
                            print(j)
                        print()
                    else:    # if there's no diseases - we print this message
                        print("    Lista chorób pacjenta jest pusta.\n")

    def szukaj_przychodnie(self, nazwa):  # this function looks for a hospital and returns a boolean whether
                                          # it's been found or not
        znaleziono = False
        for i in self.lista_przychodni:
            if i.nazwa == nazwa:
                znaleziono = True
                break

        return znaleziono

    def szukaj_pacjenta(self, nazwisko):  # this function looks for a patient and returns a boolean whether
                                          # they've been found or not
        znaleziono = False
        for i in self.lista_przychodni:
            for k in i.lista_pacjentow:
                if k.nazwisko == nazwisko:
                    znaleziono = True
                    break

        return znaleziono

    def przepisz_pacjenta(self, nazwisko, przychodnia):  # this function reassigns a patient from one hospital
                                                         # to another
        for i in self.lista_przychodni:    # looking for the patient
            for k in i.lista_pacjentow:
                if k.nazwisko == nazwisko:    # once we found them - remove them from their current hospital
                    i.lista_pacjentow.remove(k)
                    for j in self.lista_przychodni:    # now looking for the new hospital
                        if j.nazwa == przychodnia:    # and add the patient to this hospital
                            j.lista_pacjentow.append(k)
                            self.zapisz_do_pliku()    # update the file and print the message
                            return f"    Przepisano pacjenta do {przychodnia}\n"

    def pokaz_pacjenta(self, nazwisko):  # this function displays particular patient's data
                                         # their first and last name with their hospital
        for i in self.lista_przychodni:
            for k in i.lista_pacjentow:
                if k.nazwisko == nazwisko:
                    print("    Pacjent:")
                    print(f"    Imię: {k.imie}, Nazwisko: {k.nazwisko}, Przychodnia: {i.nazwa}\n")

    def ilosc_pacjentow(self, nazwa_przychodni):  # this function tells the user how many patients in a hospital

        for i in self.lista_przychodni:    # looking for the hospital
            if i.nazwa == nazwa_przychodni:    # once we found it we check if there are any patients
                if len(i.lista_pacjentow) > 0:    # if there are any patients, we print their number
                    print(f"    Przychodnia: {i.nazwa}, Ilość pacjentów: {len(i.lista_pacjentow)}\n")
                else:    # if there's no patients, we inform the user there are no patients in this hospital
                    print("    Lista pacjentów w tej przychodni jest pusta.\n")

    def statystyka_chorob(self):  # this function shows the disease frequencies
        choroby = set()    # creating a set of diseases
        for i in self.lista_przychodni:    # loop through every hospital, then through every patient and adding
                                           # the diseases to our set
            for k in i.lista_pacjentow:
                for j in k.lista_chorob:
                    choroby.add(j)

        dictionary = {}    # creating a dict of diseases so we can assign the frequency to every disease
        for i in choroby:    # looping through our set of unique diseases
            ilosc = 0    # counting variable to count the frequency of the particular disease
            for j in self.lista_przychodni:    # once again looping through every hospital, then through every patient,
                                               # and then through their list of diseases
                                               # to check, if the patient has the disease
                for k in j.lista_pacjentow:
                    for l in k.lista_chorob:
                        if l == i:   # if they do, then add one to our count variable
                            ilosc += 1
            dictionary[i] = ilosc    # assign the value that we got in the end of the loop to a key of disease
        if len(dictionary) > 0:    # if we found any diseases - we print the name and the frequency
            for i in dictionary:
                print(f"    Choroba: {i}, częstość występowania: {dictionary[i]}")
        else:    # if we didn't - we inform the user about it
            print("    Brak takiej choroby.")
        print()
