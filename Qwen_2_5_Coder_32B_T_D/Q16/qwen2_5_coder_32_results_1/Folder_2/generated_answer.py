def sum_even_ints_inclusive(int_list):
    if len(int_list) < 40:
        return 0
    return sum((num for idx, num in enumerate(int_list[15:40]) if idx + 15 >= 15 and idx + 15 <= 39 and (num % 2 == 0)))