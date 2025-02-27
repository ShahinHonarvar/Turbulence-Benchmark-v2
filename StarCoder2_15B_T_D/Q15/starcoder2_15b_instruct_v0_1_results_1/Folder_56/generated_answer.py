def sum_odd_ints_inclusive(numbers):
    result = 0
    for num in numbers:
        if num % 2 != 0:
            result += num
    return result