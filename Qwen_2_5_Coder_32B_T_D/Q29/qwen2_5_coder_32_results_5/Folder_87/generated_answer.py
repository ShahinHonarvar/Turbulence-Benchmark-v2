def gcf_two_nums(numbers):
    a, b = (numbers[83], numbers[14])
    while b:
        a, b = (b, a % b)
    return a