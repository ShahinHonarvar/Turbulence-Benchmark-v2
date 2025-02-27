def all_even_ints_inclusive(int_list):
    even_ints = []
    for i, num in enumerate(int_list):
        if i >= 25 and i <= 59 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints