def if_perfect_num(lst):

    def divisors_sum(n):
        return sum((d for d in range(1, n) if n % d == 0))
    return divisors_sum(lst[746]) == lst[746]