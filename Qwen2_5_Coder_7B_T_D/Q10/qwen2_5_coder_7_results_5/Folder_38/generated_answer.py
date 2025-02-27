def all_odd_ints_exclusive(numbers):
    return [num for idx, num in enumerate(numbers, start=1) if idx > 15 and idx < 40 and (num % 2 != 0)]