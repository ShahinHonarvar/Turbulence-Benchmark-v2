def gcf_two_nums(numbers):
    a = numbers[47]
    b = numbers[22]
    while b:
        a, b = (b, a % b)
    return a