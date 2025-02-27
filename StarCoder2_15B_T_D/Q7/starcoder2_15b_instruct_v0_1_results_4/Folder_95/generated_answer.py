def all_even_ints_inclusive(ints):
    even_ints = []
    for i, num in enumerate(ints):
        if i >= 82 and i <= 86 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints