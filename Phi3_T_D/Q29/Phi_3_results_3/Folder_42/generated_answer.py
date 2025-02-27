def gcf_two_nums(numbers):
    a = numbers[90]
    b = numbers[84]
    while b:
        a, b = (b, a % b)
    return a