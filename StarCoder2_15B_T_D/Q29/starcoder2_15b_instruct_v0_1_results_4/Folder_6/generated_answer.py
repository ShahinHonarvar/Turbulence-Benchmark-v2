def gcf_two_nums(numbers):
    return gcf(numbers[25], numbers[80])

def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a