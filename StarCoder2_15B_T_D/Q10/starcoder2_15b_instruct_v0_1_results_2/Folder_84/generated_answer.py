def all_odd_ints_exclusive(integers):
    odd_ints = []
    for index, num in enumerate(integers):
        if index >= 50 and index < 92 and (num % 2 == 1):
            odd_ints.append(num)
    return odd_ints