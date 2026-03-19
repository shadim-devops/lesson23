contacts = {}
next_id = 1

while True:
    print("\nKsiążka adresowa")
    print("1. Dodaj kontakt")
    print("2. Pokaż wszystkie kontakty")
    print("3. Szukaj kontakt")
    print("4. Usuń kontakt")
    print("5. Edytuj kontakt")
    print("6. Wyjście")

    choice = input("Wybierz opcję: ")

    if choice == "1":
        name = input("Imię: ")
        surname = input("Nazwisko: ")
        phone = input("Telefon: ")
        email = input("Email: ")

        if not phone.isdigit():
            print("Telefon powinien zawierać tylko cyfry")
            continue

        contacts[next_id] = {
            "imie": name,
            "nazwisko": surname,
            "telefon": phone,
            "email": email
        }

        print("Kontakt dodany")
        next_id += 1

    elif choice == "2":
        if not contacts:
            print("Brak kontaktów")
        else:
            for cid, data in contacts.items():
                print(cid, data)

    elif choice == "3":
        search = input("Podaj imię lub nazwisko: ").lower()

        found = False

        for cid, data in contacts.items():
            if search in data["imie"].lower() or search in data["nazwisko"].lower():
                print(cid, data)
                found = True

        if not found:
            print("Nie znaleziono kontaktu")

    elif choice == "4":
        cid = int(input("Podaj ID kontaktu do usunięcia: "))

        if cid in contacts:
            del contacts[cid]
            print("Kontakt usunięty")
        else:
            print("Nie znaleziono kontaktu")

    elif choice == "5":
        cid = int(input("Podaj ID kontaktu do edycji: "))

        if cid in contacts:
            name = input("Nowe imię: ")
            surname = input("Nowe nazwisko: ")
            phone = input("Nowy telefon: ")
            email = input("Nowy email: ")

            contacts[cid] = {
                "imie": name,
                "nazwisko": surname,
                "telefon": phone,
                "email": email
            }

            print("Kontakt zaktualizowany")
        else:
            print("Nie znaleziono kontaktu")

    elif choice == "6":
        print("Koniec programu")
        break

    else:
        print("Niepoprawna opcja")