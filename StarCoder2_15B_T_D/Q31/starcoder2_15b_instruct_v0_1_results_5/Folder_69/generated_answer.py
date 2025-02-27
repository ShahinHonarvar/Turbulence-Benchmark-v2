def if_perfect_num(lst):

    def is_perfect_num(n):
        divisors = [d for d in range(1, n) if n % d == 0]
        return sum(divisors) == n
    return is_perfect_num(lst[459])