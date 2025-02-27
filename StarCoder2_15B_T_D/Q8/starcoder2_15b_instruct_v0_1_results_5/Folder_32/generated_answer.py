def all_even_ints_exclusive(int_list):
    output = []
    for i in range(11, 76):
        if int_list[i] % 2 == 0:
            output.append(int_list[i])
    return output