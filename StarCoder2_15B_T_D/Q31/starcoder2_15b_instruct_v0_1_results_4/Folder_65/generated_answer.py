def if_perfect_num(l):
    if l[35] == sum((i for i in range(1, l[35]) if l[35] % i == 0)):
        return True
    return False