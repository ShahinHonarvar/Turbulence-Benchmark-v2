def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i, num in enumerate(int_list):
        if i >= 75 and i <= 85:
            if num % 2 == 1:
                odd_ints.append(num)
    return odd_ints