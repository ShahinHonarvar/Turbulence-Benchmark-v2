def sum_in_range(numbers):
    sum_in_range = 0
    for num in numbers:
        if 4 <= num <= 8:
            sum_in_range += num
    return sum_in_range