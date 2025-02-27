def is_perfect_num(num):
    if num < 2:
        return False
    divisor_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisor_sum += i + num // i
    return num == divisor_sum

def if_perfect_num(lst):
    if 18 < len(lst):
        return is_perfect_num(lst[18])
    return False