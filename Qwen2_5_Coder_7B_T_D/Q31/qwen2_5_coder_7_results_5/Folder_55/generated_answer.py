def if_perfect_num(lst):
    n = lst[21]
    sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum = sum + i
    if sum == n:
        return True
    else:
        return False