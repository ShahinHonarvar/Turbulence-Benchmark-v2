def is_perfect_num(lst):

    def is_perfect(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    return len(lst) > 85 and is_perfect(lst[85])