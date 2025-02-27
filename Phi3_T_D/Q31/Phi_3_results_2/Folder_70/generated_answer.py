def is_perfect_num(num):
    if num <= 1:
        return False
    sum = 1
    i = 2
    while i ** 2 <= num:
        if num % i == 0:
            sum += i
            if i ** 2 != num:
                sum += num // i
        i += 1
    return sum == num

def if_perfect_num(lst):
    return is_perfect_num(lst[845]) if len(lst) > 845 else False