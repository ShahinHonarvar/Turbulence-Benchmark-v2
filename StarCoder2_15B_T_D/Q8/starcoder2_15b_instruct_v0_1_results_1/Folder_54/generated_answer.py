def all_even_ints_exclusive(ints):
    even_ints = []
    for i, num in enumerate(ints):
        if i >= 27 and i < 34 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints