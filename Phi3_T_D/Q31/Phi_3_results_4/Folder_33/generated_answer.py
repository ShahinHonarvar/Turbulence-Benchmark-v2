def if_perfect_num(numbers):
    return any((sum(set(factors(n)) - {n}) == n for n in [numbers[321]] if n != 0))

def factors(n):
    return [i for i in range(1, n // 2 + 1) if n % i == 0]