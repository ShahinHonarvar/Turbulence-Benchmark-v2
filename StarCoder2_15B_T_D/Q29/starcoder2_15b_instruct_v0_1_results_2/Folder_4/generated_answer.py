def gcf_two_nums(numbers):
    num_1 = numbers[76]
    num_2 = numbers[57]
    if num_1 > num_2:
        smaller = num_2
    else:
        smaller = num_1
    for i in range(1, smaller + 1):
        if num_1 % i == 0 and num_2 % i == 0:
            gcf = i
    return gcf