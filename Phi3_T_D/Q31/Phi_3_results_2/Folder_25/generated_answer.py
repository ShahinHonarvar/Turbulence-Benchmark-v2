def is_perfect_number(num):
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_divisors == num

def if_perfect_num(lst):
    if len(lst) > 90:
        return is_perfect_number(lst[90])
    else:
        return False