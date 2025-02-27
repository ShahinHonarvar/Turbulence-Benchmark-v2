def sum_odd_ints_inclusive(int_list):
    return sum((num for num in int_list[50:201] if num % 2 != 0)) + (int_list[200] % 2 != 0 and int_list[200])