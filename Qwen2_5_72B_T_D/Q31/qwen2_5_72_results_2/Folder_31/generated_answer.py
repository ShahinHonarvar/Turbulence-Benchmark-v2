def if_perfect_num(lst):

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                sum = sum + i
                if i * i != n:
                    sum = sum + n // i
                i += 1
        return sum == n and n != 1
    return is_perfect(lst[66]) if len(lst) > 66 else False