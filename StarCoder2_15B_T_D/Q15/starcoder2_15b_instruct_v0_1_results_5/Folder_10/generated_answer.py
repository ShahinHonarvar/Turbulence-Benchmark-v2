def sum_odd_ints_inclusive(numbers):
    sum = 0
    for num in numbers[25:60]:
        if num % 2 != 0:
            sum += num
    return sum