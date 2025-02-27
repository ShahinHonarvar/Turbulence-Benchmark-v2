def is_perfect_number(n):
    if n <= 1:
        return False
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
        i += 1
    return sum == n

def if_perfect_num(lst):
    return is_perfect_number(lst[685]) if len(lst) > 685 else False