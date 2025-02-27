def if_perfect_num(lst):

    def is_perfect(n):
        sum_ = 0
        for i in range(1, n):
            if n % i == 0:
                sum_ += i
        return sum_ == n
    return is_perfect(lst[23]) if len(lst) > 23 else False