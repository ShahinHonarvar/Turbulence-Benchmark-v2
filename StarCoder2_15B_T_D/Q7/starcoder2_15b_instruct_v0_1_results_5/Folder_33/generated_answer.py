def all_even_ints_inclusive(ints_list):
    even_ints = []
    for i, num in enumerate(ints_list):
        if i >= 667 and i <= 774 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints