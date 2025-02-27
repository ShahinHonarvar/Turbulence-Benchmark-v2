def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf_87_20 = gcd(numbers[87] if len(numbers) > 87 else 0, numbers[20] if len(numbers) > 20 else 0)
    gcf_result = gcd(gcf_87_20, numbers[36])
    return gcf_result