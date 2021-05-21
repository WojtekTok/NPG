def adding_words(): # funkcja dodaje nowe slowa do bazy lub nie jesli juz dane slowo w niej jest
    print("Podaj slowo ktore chcesz dodac po angielsku:")
    english_given = input()

    with open("AngielskaBaza.txt", "r+") as english_write:
        list_ang_words_str = [elem.rstrip() for elem in english_write.readlines()]

        if english_given.lower() not in list_ang_words_str: # sprawdzam czy słowo jest już w bazie i wyświetlam komunikat
            english_write.write( '\n' + english_given.lower())
            english_write.close()

            print("Podaj jego odpowiednik po polsku:")
            polish_given = input()
            with open("PolskaBaza.txt", "a+") as polish_write:
                polish_write.write( '\n' + polish_given.lower())
                polish_write.close()

        else:
            print("to słowo jest już w bazie!")

#na razie basic bez podzialu na poziomy trudnosci