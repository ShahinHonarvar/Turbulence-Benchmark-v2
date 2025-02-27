def gcf_two_nums(numbers):
    a, b = (numbers[59], numbers[93])
    while b != 0:
        a, b = (b, a % b)
    return a