def all_odd_ints_inclusive(int_list):
    result = []
    for i, num in enumerate(int_list):
        if i >= 13 and i <= 68:
            if num % 2 == 1:
                result.append(num)
    return result