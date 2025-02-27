def is_perfect_num(num):
    if num < 1:
        return False
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

def if_perfect_num(lst):
    if len(lst) > 64:
        return is_perfect_num(lst[64])
    else:
        return False