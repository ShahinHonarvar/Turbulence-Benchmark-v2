def is_perfect(n):
    sum_div = sum([x for x in range(1, n // 2 + 1) if n % x == 0])
    return sum_div == n

def if_perfect_num(lst):
    length = len(lst)
    if length >= 454:
        return is_perfect(lst[453])
    else:
        return False