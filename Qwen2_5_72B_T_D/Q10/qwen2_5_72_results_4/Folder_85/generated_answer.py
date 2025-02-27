def all_odd_ints_exclusive(numbers):
    return [num for num in numbers[5:] + numbers[:4] if num % 2 != 0]