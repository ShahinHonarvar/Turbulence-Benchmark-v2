def sum_of_divisors_in_range(n):

    def divisors(num):
        factors = set()
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.add(i)
                factors.add(num // i)
        return factors
    div_sum = sum((d for d in divisors(n) if 5 <= d <= 8))
    return div_sum