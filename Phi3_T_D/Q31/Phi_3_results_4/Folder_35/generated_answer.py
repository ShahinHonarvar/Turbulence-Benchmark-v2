def is_perfect_num(num):
    return sum([i for i in range(1, num) if num % i == 0]) == num

def if_perfect_num(lst):
    if len(lst) > 993:
        return is_perfect_num(lst[993])
    return False