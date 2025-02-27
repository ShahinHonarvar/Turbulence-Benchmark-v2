def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    first_num = numbers[24] if 24 < len(numbers) else 0
    second_num = numbers[45] if 45 < len(numbers) else 0
    third_num = numbers[38] if 38 < len(numbers) else 0
    gcf = gcd(gcd(first_num, second_num), third_num)
    return gcf