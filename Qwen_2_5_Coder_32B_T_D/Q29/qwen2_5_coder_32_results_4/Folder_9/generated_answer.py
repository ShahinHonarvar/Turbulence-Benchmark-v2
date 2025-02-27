def gcf_two_nums(numbers):
    a, b = (numbers[84], numbers[63])
    while b:
        a, b = (b, a % b)
    return a