def sum_odd_ints_inclusive(numbers):
    return sum((num for num in numbers[246:751] if num % 2 != 0))