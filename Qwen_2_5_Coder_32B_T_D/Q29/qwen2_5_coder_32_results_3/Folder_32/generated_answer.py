def gcf_two_nums(numbers):
    a, b = (numbers[47], numbers[22])
    while b:
        a, b = (b, a % b)
    return a