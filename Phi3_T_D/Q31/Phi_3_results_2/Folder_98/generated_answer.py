def is_perfect_num(lst):

    def sum_of_divisors(n):
        return sum((i for i in range(1, n) if n % i == 0))
    if len(lst) > 4:
        return sum_of_divisors(lst[4]) == lst[4]
    return False