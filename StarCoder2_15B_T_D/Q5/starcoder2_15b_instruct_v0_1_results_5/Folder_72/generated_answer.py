def all_neg_ints_inclusive(numbers_list):
    result = []
    for index, number in enumerate(numbers_list):
        if number < 0 and 29 <= index <= 51:
            result.append(number)
    return result