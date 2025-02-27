def is_perfect_number(num):
    sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_of_divisors == num

def if_perfect_num(lst):
    if 19 < len(lst):
        return is_perfect_number(lst[19])
    return False