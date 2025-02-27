def if_perfect_num(lst):
    try:
        target_num = lst[87]
    except IndexError:
        return False
    divisors = [i for i in range(1, target_num) if target_num % i == 0]
    return sum(divisors) == target_num