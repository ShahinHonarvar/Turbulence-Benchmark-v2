def is_perfect_num(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

def if_perfect_num(lst):
    if 194 < len(lst):
        return is_perfect_num(lst[194])
    return False