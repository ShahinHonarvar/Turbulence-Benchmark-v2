def if_perfect_num(lst):
    if len(lst) > 16 and is_perfect(lst[16]):
        return True
    return False

def is_perfect(num):
    if num < 2:
        return False
    sum = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            sum += i
            if i != num // i:
                sum += num // i
        i += 1
    return sum == num