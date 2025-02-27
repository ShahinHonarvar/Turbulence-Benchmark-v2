def if_perfect_num(lst):

    def is_perfect(n):
        sum_factors = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum_factors += i + n // i
        return n == sum_factors and n != 1
    return is_perfect(lst[51]) if len(lst) > 51 else False