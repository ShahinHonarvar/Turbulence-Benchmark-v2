def gcf_three_nums(numbers):
    gcf = numbers[90]
    for i in range(91, 97):
        gcf = gcd(gcf, numbers[i])
    return gcf

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)