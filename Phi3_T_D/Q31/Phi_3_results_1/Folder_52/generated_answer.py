def if_perfect_num(lst):
    if len(lst) > 478:
        return all_divisors_sum(lst[478]) == lst[478]
    return False

def all_divisors_sum(num):
    sum_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i
            if i != num // i:
                sum_divisors += num // i
    return sum_divisors