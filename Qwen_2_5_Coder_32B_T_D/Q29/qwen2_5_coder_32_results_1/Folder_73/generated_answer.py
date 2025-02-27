def gcf_two_nums(numbers):
    a, b = (numbers[51], numbers[27])
    while b:
        a, b = (b, a % b)
    return a