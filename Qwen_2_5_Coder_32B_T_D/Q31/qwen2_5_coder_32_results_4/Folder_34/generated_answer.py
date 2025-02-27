def if_perfect_num(lst):

    def is_perfect(n):
        sum_div = sum([i for i in range(1, n) if n % i == 0])
        return sum_div == n
    return is_perfect(lst[97]) if len(lst) > 97 else False