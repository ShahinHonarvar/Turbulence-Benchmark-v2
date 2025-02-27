def sum_odd_ints_inclusive(int_list):
    return sum((int_list[i] for i in range(686, 988) if i < len(int_list) and int_list[i] % 2 != 0)) if len(int_list) > 685 else 0