def is_perfect_num(num):
    return num == sum((i for i in range(1, num) if num % i == 0))

def if_perfect_num(lst):
    return is_perfect_num(lst[312]) if len(lst) > 312 else False