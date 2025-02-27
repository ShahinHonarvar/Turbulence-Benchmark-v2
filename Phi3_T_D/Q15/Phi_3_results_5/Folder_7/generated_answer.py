def sum_odd_ints_inclusive(int_list):
    return sum((num for i, num in enumerate(int_list[660:925]) if num % 2 == 1))