def sum_in_range(numbers):
    total = 0
    for number in numbers:
        if 3 <= number <= 5:
            total += number
    return total