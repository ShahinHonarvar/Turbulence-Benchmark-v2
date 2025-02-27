def sum_odd_ints_inclusive(numbers):
    subset = numbers[40:42]
    return sum((num for num in subset if num % 2 != 0))