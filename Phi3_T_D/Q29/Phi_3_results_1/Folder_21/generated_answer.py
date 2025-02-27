def gcf_two_nums(numbers):
    idx198, idx212 = (198, 212)

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(numbers[idx198], numbers[idx212])