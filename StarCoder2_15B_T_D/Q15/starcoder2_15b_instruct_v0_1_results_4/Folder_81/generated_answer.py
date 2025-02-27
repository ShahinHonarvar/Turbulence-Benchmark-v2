def sum_odd_ints_inclusive(numbers):
    return sum((num for num in numbers[10:101] if num % 2 == 1))