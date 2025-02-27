def gcf_two_nums(numbers):
    a = numbers[37]
    b = numbers[30]
    while b:
        a, b = (b, a % b)
    return a