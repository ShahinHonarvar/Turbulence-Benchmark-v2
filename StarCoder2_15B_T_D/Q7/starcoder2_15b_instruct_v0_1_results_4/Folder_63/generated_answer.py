def all_even_ints_inclusive(int_list):
    even_ints = []
    for idx, num in enumerate(int_list):
        if idx >= 22 and idx <= 88 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints