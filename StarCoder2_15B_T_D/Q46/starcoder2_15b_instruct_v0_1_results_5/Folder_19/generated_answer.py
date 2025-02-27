def gcf_three_nums(numbers):
    a, b, c = (numbers[40], numbers[15], numbers[99])
    while b != 0:
        a, b = (b, a % b)
    return a