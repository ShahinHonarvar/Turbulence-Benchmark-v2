def sum_even_ints_inclusive(int_list):
    return sum((int_list[i] for i in range(50, 55) if i < len(int_list) and int_list[i] % 2 == 0))