def gcf_two_nums(numbers):
    a = numbers[166]
    b = numbers[106]
    while b:
        a, b = (b, a % b)
    return a