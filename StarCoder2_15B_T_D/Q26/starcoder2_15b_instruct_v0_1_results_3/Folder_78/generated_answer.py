def sum_in_range(list_of_integers):
    sum_of_integers = 0
    for integer in list_of_integers:
        if 90 <= integer <= 97:
            sum_of_integers += integer
    return sum_of_integers