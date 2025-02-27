def gcf_three_nums(numbers):
    num_25 = numbers[25]
    num_76 = numbers[76]
    num_57 = numbers[57]
    gcf = num_25
    for i in range(2, min(num_76, num_57) + 1):
        if num_76 % i == 0 and num_57 % i == 0:
            gcf = i
    return gcf