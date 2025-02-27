def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    try:
        return gcd(numbers[372], numbers[752])
    except IndexError:
        return 'Indices out of range'