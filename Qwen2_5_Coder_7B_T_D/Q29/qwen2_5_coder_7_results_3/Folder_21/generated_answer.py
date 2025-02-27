def gcf_two_nums(numbers):
    a = numbers[198]
    b = numbers[212]
    while b:
        a, b = (b, a % b)
    return a