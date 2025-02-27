def gcf_two_nums(numbers):
    a = numbers[85]
    b = numbers[33]
    while b != 0:
        a, b = (b, a % b)
    return a