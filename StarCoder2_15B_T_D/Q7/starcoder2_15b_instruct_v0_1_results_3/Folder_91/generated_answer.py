def all_even_ints_inclusive(lst):
    all_even_ints = []
    for i in range(len(lst)):
        if i >= 0 and i <= 5:
            if lst[i] % 2 == 0:
                all_even_ints.append(lst[i])
    return all_even_ints