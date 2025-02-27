def if_perfect_num(lst):
    num = lst[21]
    divisors = [divisor for divisor in range(1, num) if num % divisor == 0]
    return sum(divisors) == num