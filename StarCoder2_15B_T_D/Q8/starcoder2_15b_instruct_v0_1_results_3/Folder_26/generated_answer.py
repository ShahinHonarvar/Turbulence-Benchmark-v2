def all_even_ints_exclusive(integers):
    even_ints = []
    for i, num in enumerate(integers):
        if num % 2 == 0 and i in range(44, 78):
            even_ints.append(num)
    return even_ints