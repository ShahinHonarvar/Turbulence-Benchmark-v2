def all_odd_ints_inclusive(numbers):
    odd_ints = []
    for i in range(10, 67):
        if numbers[i] % 2 == 1:
            odd_ints.append(numbers[i])
    return odd_ints