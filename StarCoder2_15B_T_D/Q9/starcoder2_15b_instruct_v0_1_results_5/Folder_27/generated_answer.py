def all_odd_ints_inclusive(numbers):
    odd_ints = []
    for index, num in enumerate(numbers):
        if index >= 66 and index <= 93 and (num % 2 != 0):
            odd_ints.append(num)
    return odd_ints