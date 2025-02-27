def if_perfect_num(lst):
    if len(lst) > 15:
        num = lst[15]
        sum_of_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_of_divisors += i
        return sum_of_divisors == num
    else:
        return False