def is_perfect_num(num):
    return num == sum((i for i in range(1, num) if num % i == 0))

def if_perfect_num(lst):
    return is_perfect_num(lst[38]) if len(lst) > 38 else False