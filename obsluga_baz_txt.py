import random


def check_polish_word(random_number):  # funkcja zwraca slowo o danym indeksie z bazy pol
    with open("PolskaBaza.txt", mode="r") as pol_base_file:
        pol_base = pol_base_file.readlines()

    pol_base_file.close()
    return pol_base[random_number]


def check_ang_word(random_number):  # funkcja zwraca slowo o danym indeksie z bazy ang
    with open("AngielskaBaza.txt", mode="r") as ang_base_file:
        ang_base = ang_base_file.readlines()

    ang_base_file.close()
    return ang_base[random_number]


def ask_user(random_number):  # funkcja pyta jeden raz uzytkownika o slowo o danym indeksiem, sprawdza czy odpowiedzial dobrze i zwraca 1 lub 0
    word = check_polish_word(random_number)
    correct_ans = check_ang_word(random_number).strip()

    print("Podaj angielski odpowiednik słowa:", word, end="")  # pytam uzytkownika o wylosowane slowo
    ans = input()  # odpowiedz uzytkownika
    return (int)(ans.lower() == correct_ans)  # zwracam 1 jezeli uzytkownik zgadl lub 0 jak nie zgadl


def draw_from_whole_base():  # losuje pytanie z całej bazy (działa również gdy już dodamy swoje słowa)
    with open("AngielskaBaza.txt", mode="r") as base_to_draw:
        numer_of_word = base_to_draw.readlines()
        drawed_number = random.randrange(1, len(numer_of_word))
        base_to_draw.close()
    return drawed_number


def ask_user_times(
        number_of_questions):  # glowna funkcja przyjmuje argument ile pytan ma zadac uzytkownikowi, zwraca wynik( liczbe poprawnych odp)
    list = []  # lista tych numerow, zapobieganie powatrzaniou pytan
    current_result = 0  # poczatkowy wynik do ktorego funkcja dodaje

    i = 0
    while (i < number_of_questions):  # tyle pytan ile funkcja dostala jako argument
        random_number = draw_from_whole_base()
        if random_number not in list:
            list.append(random_number)
            current_result += ask_user(random_number)  # dodaje +1 jak uzytkownik dobrze odpowie
            i += 1
        else:
            continue
    return current_result  # zwraca liczbe poprawnych odp przez uzytkownika


def save_result_to_txt(
        result):  # funkcja dostaje wynik uzytkownika i zapisuje go w nowej lini pliku txt results_user.txt
    result_str = (str)(result)
    with open("results_user.txt", mode="a") as result_file:
        result_file.writelines(result_str)
        result_file.writelines("\n")
        result_file.close()
