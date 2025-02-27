def all_odd_ints_exclusive(ints):
    odd_ints = []
    for i, num in enumerate(ints):
        if i >= 20 and i < 51 and (num % 2 == 1):
            odd_ints.append(num)
    return odd_ints