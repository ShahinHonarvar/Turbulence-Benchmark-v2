def gcf_two_nums(numbers):
    num1 = numbers[60]
    num2 = numbers[64]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1