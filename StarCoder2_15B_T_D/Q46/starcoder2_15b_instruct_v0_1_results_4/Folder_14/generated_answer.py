def gcf_three_nums(numbers):
    return gcf(numbers[17], gcf(numbers[88], numbers[35]))

def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)