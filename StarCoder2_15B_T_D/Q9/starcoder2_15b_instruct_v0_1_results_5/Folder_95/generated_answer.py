def all_odd_ints_inclusive(ints):
    odd_ints = []
    for i, num in enumerate(ints):
        if i >= 82 and i <= 86 and (num % 2 != 0):
            odd_ints.append(num)
    return odd_ints