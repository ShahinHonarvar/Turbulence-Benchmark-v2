def if_perfect_num(lst):

    def is_perfect(n):
        sum_div = 0
        for i in range(1, n):
            if n % i == 0:
                sum_div += i
        return sum_div == n
    return is_perfect(lst[93])