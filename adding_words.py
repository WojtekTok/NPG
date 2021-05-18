def adding_words():
    print("Podaj slowo ktore chcesz dodac po angielsku:")
    english = input()
    
    print("Podaj jego odpowiednik po polsku:")
    polish = input()
    
    with open("AngielskaBaza.txt", "a+") as english_write:
        english_write.write('\n')
        english_write.write(english)
    english_write.close()
    
    with open("PolskaBaza.txt", "a+") as polish_write:
        polish_write.write('\n')
        polish_write.write(polish)
    polish_write.close()

#na razie basic bez podzialu na poziomy trudnosci
