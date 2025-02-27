def gcf_three_nums(numbers):
    num24 = numbers[24]
    num45 = numbers[45]
    num38 = numbers[38]
    gcf = num24
    for i in range(2, min(num24, num45, num38) + 1):
        if num24 % i == 0 and num45 % i == 0 and (num38 % i == 0):
            gcf = i
    return gcf