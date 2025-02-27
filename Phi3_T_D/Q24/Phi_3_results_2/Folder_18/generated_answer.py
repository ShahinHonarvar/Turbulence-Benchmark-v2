def sum_of_divisors_in_range(n):

    def proper_divisors(num):
        return [i for i in range(1, num // 2 + 1) if num % i == 0]
    dividends = proper_divisors(n)
    return sum(filter(lambda x: 387 <= x <= 516, dividends))