def all_even_ints_inclusive(num_list):
    return [num for num in num_list if num % 2 == 0 and 0 <= num_list.index(num) <= 2]