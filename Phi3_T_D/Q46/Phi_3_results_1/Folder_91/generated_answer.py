def gcf_three_nums(numbers):
    a, b, c = (numbers[8], numbers[9], numbers[3])
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a