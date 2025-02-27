def all_even_ints_exclusive(lst):
    even_ints = []
    for i, num in enumerate(lst):
        if i >= 18 and i < 37 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints