def sum_odd_ints_inclusive(ints):
    sum_odd = 0
    for i, num in enumerate(ints):
        if 31 <= i <= 72:
            if num % 2 == 1:
                sum_odd += num
    return sum_odd