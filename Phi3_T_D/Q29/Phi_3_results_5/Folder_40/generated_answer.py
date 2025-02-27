def gcf_two_nums(numbers):
    a, b = (numbers[7], numbers[9])
    while b:
        a, b = (b, a % b)
    return a