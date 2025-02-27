def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    first_num = numbers[38]
    second_num = numbers[52]
    third_num = numbers[69]
    return gcd(gcd(first_num, second_num), third_num)