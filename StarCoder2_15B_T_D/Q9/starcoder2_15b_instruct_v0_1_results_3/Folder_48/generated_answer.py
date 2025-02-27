def all_odd_ints_inclusive(my_list):
    result = []
    for i in range(533, 606):
        if my_list[i] % 2 == 1:
            result.append(my_list[i])
    return result