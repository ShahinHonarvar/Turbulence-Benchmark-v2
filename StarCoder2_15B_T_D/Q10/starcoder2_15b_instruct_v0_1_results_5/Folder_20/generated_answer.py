def all_odd_ints_exclusive(ints):
    odd_ints = []
    for i, num in enumerate(ints):
        if i >= 59 and i < 93 and (num % 2 == 1):
            odd_ints.append(num)
    return odd_ints