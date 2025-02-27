def gcf_three_nums(numbers):
    num1 = numbers[991]
    num2 = numbers[244]
    num3 = numbers[974]
    smaller = min(num1, num2, num3)
    for i in range(smaller, 0, -1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            return i