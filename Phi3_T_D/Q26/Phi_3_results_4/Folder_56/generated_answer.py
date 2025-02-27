def sum_in_range(numbers):
    result = 0
    for number in numbers:
        if 4 <= number <= 9:
            result += number
    return result