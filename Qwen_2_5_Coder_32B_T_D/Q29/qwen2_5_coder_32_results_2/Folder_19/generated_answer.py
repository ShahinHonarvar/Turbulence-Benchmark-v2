def gcf_two_nums(numbers):
    a, b = (numbers[66], numbers[90])
    while b:
        a, b = (b, a % b)
    return a