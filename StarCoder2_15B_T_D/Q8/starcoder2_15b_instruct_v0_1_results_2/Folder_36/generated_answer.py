def all_even_ints_exclusive(ints):
    even_ints = []
    for i in ints:
        if i % 2 == 0:
            even_ints.append(i)
    return even_ints