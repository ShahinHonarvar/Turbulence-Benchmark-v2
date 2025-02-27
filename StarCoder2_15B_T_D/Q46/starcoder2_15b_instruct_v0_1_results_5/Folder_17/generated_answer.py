def gcf_three_nums(numbers):
    gcf = numbers[20]
    for i in range(21, 62):
        gcf = gcd(gcf, numbers[i])
    return gcf