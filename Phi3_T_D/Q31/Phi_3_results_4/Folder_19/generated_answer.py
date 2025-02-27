def is_perfect_num(num):
    return num == sum([i for i in range(1, num) if num % i == 0])

def if_perfect_num(lst):
    return is_perfect_num(lst[13]) if len(lst) > 13 else False