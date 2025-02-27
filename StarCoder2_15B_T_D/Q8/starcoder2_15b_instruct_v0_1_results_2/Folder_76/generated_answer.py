def all_even_ints_exclusive(lst):
    even_ints = []
    for i, num in enumerate(lst):
        if i >= 361 and i < 643 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints