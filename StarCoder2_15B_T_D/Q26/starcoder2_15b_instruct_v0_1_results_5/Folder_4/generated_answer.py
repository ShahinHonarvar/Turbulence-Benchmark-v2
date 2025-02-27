def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 32 <= num <= 44:
            total += num
    return total