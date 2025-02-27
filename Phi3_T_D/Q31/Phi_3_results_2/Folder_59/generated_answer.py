def if_perfect_num(lst):
    if len(lst) < 3:
        return False
    number = lst[2]
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number