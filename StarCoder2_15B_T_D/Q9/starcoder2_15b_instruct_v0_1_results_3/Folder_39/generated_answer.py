def all_odd_ints_inclusive(numbers):
    odd_ints = []
    for i, num in enumerate(numbers):
        if i >= 20 and i <= 30 and (num % 2 == 1):
            odd_ints.append(num)
    return odd_ints