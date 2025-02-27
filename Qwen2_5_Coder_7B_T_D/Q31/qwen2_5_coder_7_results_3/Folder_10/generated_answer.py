def if_perfect_num(lst):
    if len(lst) > 54:
        num = lst[54]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else:
        return False