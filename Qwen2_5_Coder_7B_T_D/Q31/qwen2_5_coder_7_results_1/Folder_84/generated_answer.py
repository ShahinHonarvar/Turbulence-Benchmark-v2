def if_perfect_num(lst):
    if 685 < len(lst):
        num = lst[685]
        sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_of_divisors == num
    else:
        return False