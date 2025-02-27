def gcf_three_nums(numbers):
    num34 = numbers[34]
    num38 = numbers[38]
    num77 = numbers[77]
    if num34 < num38 < num77:
        smaller = num34
    elif num34 < num77 < num38:
        smaller = num34
    elif num38 < num34 < num77:
        smaller = num38
    elif num38 < num77 < num34:
        smaller = num38
    elif num77 < num34 < num38:
        smaller = num77
    else:
        smaller = num77
    for i in range(1, smaller + 1):
        if num34 % i == 0 and num38 % i == 0 and (num77 % i == 0):
            gcf = i
    return gcf