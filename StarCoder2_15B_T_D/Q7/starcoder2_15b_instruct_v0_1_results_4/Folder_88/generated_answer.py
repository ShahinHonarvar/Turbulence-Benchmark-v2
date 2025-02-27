def all_even_ints_inclusive(integers_list):
    even_ints = []
    for i in range(len(integers_list)):
        if integers_list[i] % 2 == 0:
            even_ints.append(integers_list[i])
    return even_ints