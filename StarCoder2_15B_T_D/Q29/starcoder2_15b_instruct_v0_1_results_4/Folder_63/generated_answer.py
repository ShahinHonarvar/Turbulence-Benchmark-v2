def gcf_two_nums(numbers):
    num_21 = numbers[21]
    num_17 = numbers[17]
    if num_21 > num_17:
        smaller = num_17
    else:
        smaller = num_21
    for i in range(1, smaller + 1):
        if num_21 % i == 0 and num_17 % i == 0:
            gcf = i
    return gcf