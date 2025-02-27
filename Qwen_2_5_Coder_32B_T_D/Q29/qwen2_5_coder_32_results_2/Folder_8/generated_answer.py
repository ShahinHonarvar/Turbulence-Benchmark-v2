def gcf_two_nums(numbers):
    a, b = (numbers[69], numbers[41])
    while b:
        a, b = (b, a % b)
    return a