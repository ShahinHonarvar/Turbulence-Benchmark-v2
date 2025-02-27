def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 99:
        raise ValueError('List too short, minimum length should be 100')
    return gcd(gcd(numbers[99], numbers[95]), numbers[80])