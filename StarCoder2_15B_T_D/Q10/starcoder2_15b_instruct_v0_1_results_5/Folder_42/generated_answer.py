def all_odd_ints_exclusive(int_list):
    result = []
    for index, element in enumerate(int_list):
        if 44 < index < 67 and element % 2 == 1:
            result.append(element)
    return result