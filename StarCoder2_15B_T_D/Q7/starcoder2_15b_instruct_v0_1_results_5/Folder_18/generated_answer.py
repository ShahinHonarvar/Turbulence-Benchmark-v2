def all_even_ints_inclusive(int_list):
    result = []
    for i in range(len(int_list)):
        if i >= 35 and i <= 49 and (int_list[i] % 2 == 0):
            result.append(int_list[i])
    return result