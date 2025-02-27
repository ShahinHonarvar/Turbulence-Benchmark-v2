def all_odd_ints_inclusive(numbers):
    odd_ints = []
    for i, num in enumerate(numbers):
        if i >= 43 and i <= 51 and (num % 2 == 1):
            odd_ints.append(num)
    return odd_ints