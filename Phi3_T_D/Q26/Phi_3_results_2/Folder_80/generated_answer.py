def sum_in_range(list_of_integers):
    total = sum((num for num in list_of_integers if -798 <= num <= -379))
    return total if total != 0 else 0