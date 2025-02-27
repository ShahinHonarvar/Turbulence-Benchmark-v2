def all_even_ints_exclusive(ints):
    even_ints = []
    for i, num in enumerate(ints):
        if i >= 38 and i < 81 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints