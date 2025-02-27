def gcf_two_nums(numbers):
    num1 = numbers[38]
    num2 = numbers[77]
    smaller = min(num1, num2)
    for i in range(smaller, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i