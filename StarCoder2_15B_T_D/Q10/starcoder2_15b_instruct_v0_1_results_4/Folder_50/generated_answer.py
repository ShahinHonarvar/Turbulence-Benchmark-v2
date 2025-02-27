def all_odd_ints_exclusive(input_list):
    result = []
    for i in range(len(input_list)):
        if i >= 70 and i < 98:
            if input_list[i] % 2 != 0:
                result.append(input_list[i])
    return result