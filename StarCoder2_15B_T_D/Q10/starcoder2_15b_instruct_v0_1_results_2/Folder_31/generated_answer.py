def all_odd_ints_exclusive(int_list):
    result = []
    for i in range(87, 95):
        if i < len(int_list) and int_list[i] % 2 == 1:
            result.append(int_list[i])
    return result