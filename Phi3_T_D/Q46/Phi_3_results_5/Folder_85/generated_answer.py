def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 49 or len(numbers) < 46 or len(numbers) < 13:
        return None
    common_factor = gcd(numbers[49], numbers[46])
    return gcd(common_factor, numbers[13])