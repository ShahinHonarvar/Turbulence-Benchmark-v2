def if_perfect_num(lst):
    if 67 >= len(lst):
        return False
    num = lst[67]
    return num == sum([i for i in range(1, num) if num % i == 0])