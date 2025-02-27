def gcf_two_nums(numbers):
    a, b = (numbers[28], numbers[17])
    while b:
        a, b = (b, a % b)
    return a