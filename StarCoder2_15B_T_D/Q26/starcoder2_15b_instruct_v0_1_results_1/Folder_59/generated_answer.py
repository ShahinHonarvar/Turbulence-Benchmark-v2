def sum_in_range(numbers):
    total = 0
    for number in numbers:
        if 2 <= number <= 3:
            total += number
    return total