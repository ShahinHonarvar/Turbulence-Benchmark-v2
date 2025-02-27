def all_odd_ints_exclusive(numbers):
    odd_numbers = []
    for i, num in enumerate(numbers):
        if i >= 40 and i < 200 and (num % 2 == 1):
            odd_numbers.append(num)
    return odd_numbers