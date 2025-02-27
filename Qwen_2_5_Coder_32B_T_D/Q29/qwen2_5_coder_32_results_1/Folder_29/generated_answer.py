def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_two_nums(numbers):
    return gcd(numbers[96], numbers[57])