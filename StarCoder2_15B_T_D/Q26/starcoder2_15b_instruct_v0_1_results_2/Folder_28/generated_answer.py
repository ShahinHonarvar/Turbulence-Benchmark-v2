def sum_in_range(integers):
    sum_of_integers = 0
    for integer in integers:
        if 10 <= integer <= 97:
            sum_of_integers += integer
    return sum_of_integers