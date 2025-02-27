def if_perfect_num(lst):
    if len(lst) <= 453:
        return False
    num = lst[453]
    sum_divs = sum((i for i in range(1, num) if num % i == 0))
    return sum_divs == num