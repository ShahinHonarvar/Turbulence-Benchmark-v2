def gcf_two_nums(numbers):
    a, b = (numbers[46], numbers[13])
    while b:
        a, b = (b, a % b)
    return a