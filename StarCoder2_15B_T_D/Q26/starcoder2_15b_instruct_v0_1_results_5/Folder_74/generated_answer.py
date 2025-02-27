def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if num >= 13 and num <= 35:
            total += num
    return total