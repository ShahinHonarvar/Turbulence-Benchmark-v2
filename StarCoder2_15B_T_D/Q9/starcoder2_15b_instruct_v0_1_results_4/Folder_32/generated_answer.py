def all_odd_ints_inclusive(ints_list):
    result = []
    for i in range(len(ints_list)):
        if i >= 21 and i <= 97 and (ints_list[i] % 2 == 1):
            result.append(ints_list[i])
    return result