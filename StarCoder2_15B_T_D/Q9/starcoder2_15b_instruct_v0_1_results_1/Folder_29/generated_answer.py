def all_odd_ints_inclusive(numbers):
    odd_ints = []
    for i, num in enumerate(numbers):
        if i >= 59 and i <= 97 and (num % 2 != 0):
            odd_ints.append(num)
    return odd_ints