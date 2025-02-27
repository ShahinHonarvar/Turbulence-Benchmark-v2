def all_even_ints_exclusive(ints_list):
    even_ints = []
    for i, num in enumerate(ints_list):
        if num % 2 == 0 and 36 < i < 52:
            even_ints.append(num)
    return even_ints