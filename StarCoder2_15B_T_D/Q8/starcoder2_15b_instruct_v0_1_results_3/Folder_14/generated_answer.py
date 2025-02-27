def all_even_ints_exclusive(my_list):
    even_ints = []
    for i, num in enumerate(my_list):
        if i >= 1 and i < 7 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints