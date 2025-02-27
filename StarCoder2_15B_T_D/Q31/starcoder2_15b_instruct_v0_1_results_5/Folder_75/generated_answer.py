def if_perfect_num(lst):
    pass
    if lst[80] == sum((divisor for divisor in range(1, lst[80]) if lst[80] % divisor == 0)):
        return True
    else:
        return False