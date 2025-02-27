def all_even_ints_inclusive(lst):
    even_ints = []
    for i, num in enumerate(lst):
        if i >= 3 and i <= 5 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints