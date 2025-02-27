def is_perfect_num(lst):
    if len(lst) > 68:
        num = lst[68]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False