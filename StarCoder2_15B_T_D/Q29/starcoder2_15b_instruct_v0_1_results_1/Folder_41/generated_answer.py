def gcf_two_nums(numbers):
    num1 = numbers[23]
    num2 = numbers[27]

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    return gcf(num1, num2)