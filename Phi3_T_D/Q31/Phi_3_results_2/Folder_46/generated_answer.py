def is_perfect_num(num):
    return sum((i for i in range(1, num) if num % i == 0)) + 1 == num

def if_perfect_num(lst):
    return is_perfect_num(lst[453]) if len(lst) > 453 else False