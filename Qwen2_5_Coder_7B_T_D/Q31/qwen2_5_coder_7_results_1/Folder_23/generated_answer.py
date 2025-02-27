def if_perfect_num(lst):
    if 69 < len(lst):
        num = lst[69]
        div_sum = sum((i for i in range(1, num) if num % i == 0))
        return div_sum == num
    return False