def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if num >= 138 and num <= 858:
            total += num
    return total