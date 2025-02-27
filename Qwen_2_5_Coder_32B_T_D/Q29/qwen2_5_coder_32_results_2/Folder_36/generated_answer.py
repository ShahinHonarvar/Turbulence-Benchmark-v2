def gcf_two_nums(numbers):
    a, b = (numbers[429], numbers[289])
    while b:
        a, b = (b, a % b)
    return a