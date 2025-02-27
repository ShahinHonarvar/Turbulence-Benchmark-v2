def all_pos_ints_inclusive(list_of_ints):
    result = []
    for i in range(len(list_of_ints)):
        if i >= 40 and i <= 80:
            if list_of_ints[i] > 0:
                result.append(list_of_ints[i])
    return result