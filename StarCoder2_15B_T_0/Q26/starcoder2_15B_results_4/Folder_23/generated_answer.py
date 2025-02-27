def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 50 <= num <= 92:
            total += num
    return total