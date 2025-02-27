def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 2 <= num <= 7:
            total += num
    return total