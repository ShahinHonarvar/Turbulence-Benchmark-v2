def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 100:
        return 'Index out of range'
    first = gcd(numbers[92], numbers[69])
    return gcd(first, numbers[95])