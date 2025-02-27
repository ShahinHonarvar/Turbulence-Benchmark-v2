def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 4 <= num <= 8:
            total += num
    return total