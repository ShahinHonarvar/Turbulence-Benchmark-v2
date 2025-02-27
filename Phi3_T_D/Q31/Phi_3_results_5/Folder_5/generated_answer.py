def if_perfect_num(integers):
    try:
        num = integers[67]
        sum_divisors = sum((i for i in range(1, num) if num % i == 0))
        return num == sum_divisors
    except IndexError:
        return False