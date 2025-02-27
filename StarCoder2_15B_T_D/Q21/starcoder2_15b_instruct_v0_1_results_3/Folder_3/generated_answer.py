def all_ints_div_by_num(integers):
    result = []
    for i in range(25, 60):
        if integers[i] % -26 == 0:
            result.append(integers[i])
    return result