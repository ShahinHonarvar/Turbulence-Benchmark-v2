def is_perfect_num(n):
    if n < 2:
        return False
    divisor_sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i
    return divisor_sum == n

def if_perfect_num(lst):
    return is_perfect_num(lst[69]) if len(lst) > 69 else False