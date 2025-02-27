def all_odd_ints_inclusive(int_list):
    if not int_list:
        return []
    odd_ints = [num for num in int_list if num % 2 == 1]
    if not odd_ints[28:39]:
        return []
    return odd_ints[28:39]