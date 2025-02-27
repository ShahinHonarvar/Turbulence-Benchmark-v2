def gcf_two_nums(numbers):
    gcf = 1
    num1 = numbers[48]
    num2 = numbers[74]
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf