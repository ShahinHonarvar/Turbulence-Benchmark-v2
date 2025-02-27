def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    result = gcd(numbers[36], numbers[85])
    return gcd(result, numbers[83])