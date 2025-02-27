def gcf_two_nums(numbers):

    def find_gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 49:
        return find_gcd(numbers[28], numbers[49])
    else:
        return None