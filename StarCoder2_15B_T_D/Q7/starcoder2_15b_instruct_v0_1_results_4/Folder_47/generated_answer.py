def all_even_ints_inclusive(input_list):
    if len(input_list) < 2:
        return []
    even_ints = []
    for i in range(37, len(input_list)):
        if input_list[i] % 2 == 0:
            even_ints.append(input_list[i])
    return even_ints