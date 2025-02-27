def sum_odd_ints_inclusive(ints):
    sum = 0
    for i, num in enumerate(ints):
        if num % 2 == 1 and 62 <= i <= 78:
            sum += num
    return sum