def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if -23 <= num <= 64:
            total += num
    return total