import random
from tkinter import *

root = Tk()  # tworzę 'okienko'
root.title("Fiszki")
root.geometry('500x500')

def check_polish_word(random_number):   #funkcja zwraca slowo o danym indeksie z bazy pol
    with open("PolskaBaza.txt", "r") as pol_base_file:
        pol_base = pol_base_file.readlines()

    pol_base_file.close()
    return pol_base[random_number]

def check_ang_word(random_number): # funkcja zwraca slowo o danym indeksie z bazy ang
    with open("AngielskaBaza.txt", "r") as ang_base_file:
        ang_base = ang_base_file.readlines()

    ang_base_file.close()
    return ang_base[random_number]


def ask_user(random_number): # funkcja pyta jeden raz uzytkownika o slowo o danym indeksiem, sprawdza czy odpowiedzial dobrze i zwraca 1 lub 0
    word = check_polish_word(random_number)
    correct_ans = check_ang_word(random_number).strip()
    myLabel4 = Label(root, text="Podaj angielski odpowiednik słowa:" + word).place(x=100,y=250)
    button_4.place(x=300, y=350)
    e = Entry(root, width=35, borderwidth=5)
    e.place(x=130, y=300)
    root.update()
    button_4.wait_variable(var)
    print("Podaj angielski odpowiednik słowa:", word, end="") # pytam uzytkownika o wylosowane slowo
    ans = str(e.get())# odpowiedz uzytkownika
    e.delete(0, END)
    return (int)(ans.lower() == correct_ans)  # zwracam 1 jezeli uzytkownik zgadl lub 0 jak nie zgadl

def draw_from_whole_base(): # losuje pytanie z całej bazy (działa również gdy już dodamy swoje słowa)
    with open("AngielskaBaza.txt", "r") as base_to_draw:
        numer_of_word = base_to_draw.readlines()
        drawed_number = random.randrange(1, len(numer_of_word))
        base_to_draw.close()
    return drawed_number

def ask_user_times(number_of_questions): # glowna funkcja przyjmuje argument ile pytan ma zadac uzytkownikowi, zwraca wynik( liczbe poprawnych odp)
    list = [] # lista tych numerow, zapobieganie powatrzaniou pytan
    current_result = 0  # poczatkowy wynik do ktorego funkcja dodaje
    i = 0
    while (i  < number_of_questions):  # tyle pytan ile funkcja dostala jako argument
        random_number = draw_from_whole_base()
        if random_number not in list:
            list.append(random_number)
            current_result += ask_user(random_number) # dodaje +1 jak uzytkownik dobrze odpowie
            i += 1
        else:
            continue
    return current_result # zwraca liczbe poprawnych odp przez uzytkownika

def save_result_to_txt(result): # funkcja dostaje wynik uzytkownika i zapisuje go w nowej lini pliku txt results_user.txt
    result_str = (str)(result)
    with open("results_user.txt", "a") as result_file:
        result_file.writelines('\n' + result_str)
        result_file.close()


var = IntVar()
value = 1


def callback(): #funkcja która reaguje jak sie kliknie poziom średni.
    global value
    value -= 1
    if value == 0:
        a = ask_user_times(5)
        myLabel2 = Label(root,text = "Twój wynik to " + str(a)).place(x = 150, y = 400)
        save_result_to_txt(a)
        value = 1
    else:
        pass


myLabel1 = Label(root, text = "Wybierz poziom trudnośći!").pack()

button_1 = Button(root, text='łatwy',padx=40, pady = 40, bg="green")
button_2 = Button(root, text='średni',padx=40, pady = 40, command=callback,bg="yellow")
button_3 = Button(root, text='trudny',padx=40, pady = 40,bg="red")
button_4 = Button(root, text="dalej", command=lambda: var.set(1)) #funkcje buttonów
button_1.place(x=60,y=20)
button_2.place(x=190,y=20)
button_3.place(x=320,y=20) #pozycje buttonów latwy sredni trudny


button_quit = Button(root, text="Exit Programm", command=root.quit)
button_quit.place(x= 190,y =460) #pozycja button quixt
root.mainloop()  # komenda aby okienko się nie zamknęło
