def is_perfect_num(num):
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    return sum_div == num

def if_perfect_num(lst):
    if len(lst) > 21:
        return is_perfect_num(lst[21])
    return False