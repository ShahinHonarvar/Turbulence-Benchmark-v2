def gcf_two_nums(numbers):
    num1 = numbers[29]
    num2 = numbers[53]
    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    return num1