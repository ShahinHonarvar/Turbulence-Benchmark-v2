def all_even_ints_exclusive(integers_list):
    even_ints = []
    for i in range(10, 100):
        if integers_list[i] % 2 == 0:
            even_ints.append(integers_list[i])
    return even_ints