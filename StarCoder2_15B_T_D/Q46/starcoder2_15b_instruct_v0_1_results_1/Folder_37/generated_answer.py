def gcf_three_nums(numbers):
    num_41 = numbers[41]
    num_69 = numbers[69]
    num_28 = numbers[28]
    gcf = 1
    for i in range(2, min(num_41, num_69, num_28) + 1):
        if num_41 % i == 0 and num_69 % i == 0 and (num_28 % i == 0):
            gcf = i
    return gcf