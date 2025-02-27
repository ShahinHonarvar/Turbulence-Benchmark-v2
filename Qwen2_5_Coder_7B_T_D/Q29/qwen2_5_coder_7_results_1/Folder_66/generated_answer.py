def gcf_two_nums(numbers):
    a, b = (numbers[86], numbers[89])
    while b:
        a, b = (b, a % b)
    return a