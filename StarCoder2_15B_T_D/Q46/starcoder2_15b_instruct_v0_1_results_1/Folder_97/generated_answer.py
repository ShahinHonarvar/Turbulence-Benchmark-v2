def gcf_three_nums(numbers):
    gcf = numbers[944]
    for i in range(945, 947):
        gcf = gcd(gcf, numbers[i])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a