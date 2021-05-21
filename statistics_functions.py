def show_average_last_five(): #funkcja pokazująca średnią z ostatnich (5) prób
    with open("results_user.txt", mode = "r") as result_file:
        list_of_results_int = [int(elem) for elem in result_file.readlines()]
        suma = 0

        for i in range(5): # dla 5
            suma += list_of_results_int[-i]
        result_file.close()

        return float(suma/5) # dla 5


def show_total_average(): #funkcja pokazująca średnią arytmetyczna z wszystkich wyników
    with open("results_user.txt", mode = "r") as result_file:
        list_of_results_int = [int(elem) for elem in result_file.readlines()]

        result_file.close()

        return sum(list_of_results_int)/len(list_of_results_int)

#print(show_total_average())
#print(show_average_last_five())