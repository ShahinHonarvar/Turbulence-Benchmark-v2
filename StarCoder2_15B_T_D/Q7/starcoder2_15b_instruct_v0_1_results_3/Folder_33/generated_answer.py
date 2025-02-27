def all_even_ints_inclusive(lst):
    even_ints = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and 667 <= i <= 774:
            even_ints.append(lst[i])
    return even_ints