def all_odd_ints_inclusive(int_list):
    if not int_list:
        return []
    start = 23
    end = 23
    odd_ints = []
    for i, num in enumerate(int_list):
        if i >= start and i <= end:
            if num % 2 != 0:
                odd_ints.append(num)
    return odd_ints