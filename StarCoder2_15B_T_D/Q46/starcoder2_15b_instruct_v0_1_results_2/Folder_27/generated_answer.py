def gcf_three_nums(numbers):
    num1 = numbers[76]
    num2 = numbers[64]
    num3 = numbers[28]
    gcf = num1
    while gcf != num2 and gcf != num3:
        gcf -= 1
    return gcf