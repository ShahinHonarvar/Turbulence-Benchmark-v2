def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 20 <= num <= 93:
            total += num
    return total