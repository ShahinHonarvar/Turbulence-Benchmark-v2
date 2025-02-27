def gcf_three_nums(numbers):
    gcf = numbers[307]
    for i in range(920, 463, -1):
        if numbers[i] < gcf:
            gcf = numbers[i]
    for i in range(463, 920):
        if numbers[i] < gcf:
            gcf = numbers[i]
    return gcf