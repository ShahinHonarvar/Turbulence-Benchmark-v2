def all_odd_ints_exclusive(numbers):
    odd_numbers = []
    for i, number in enumerate(numbers):
        if i >= 50 and i < 200 and (number % 2 != 0):
            odd_numbers.append(number)
    return odd_numbers