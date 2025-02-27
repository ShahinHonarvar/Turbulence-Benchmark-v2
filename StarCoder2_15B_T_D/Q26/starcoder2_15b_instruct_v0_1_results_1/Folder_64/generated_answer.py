def sum_in_range(numbers):
    sum = 0
    for n in numbers:
        if -3 <= n <= 6:
            sum += n
    return sum