def sum_even_ints_inclusive(lst):
    sum_of_evens = sum((lst[i] for i in range(667, 775) if lst[i] % 2 == 0))
    return sum_of_evens