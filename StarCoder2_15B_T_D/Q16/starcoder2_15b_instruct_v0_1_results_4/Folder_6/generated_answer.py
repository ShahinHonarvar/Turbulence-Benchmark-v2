def sum_even_ints_inclusive(ints):
    sum = 0
    for i, num in enumerate(ints):
        if num % 2 == 0 and 10 <= i <= 66:
            sum += num
    return sum