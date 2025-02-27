def gcf_two_nums(numbers):
    a = numbers[54]
    b = numbers[56]
    while b != 0:
        a, b = (b, a % b)
    return a