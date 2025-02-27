def if_perfect_num(lst):
    index = 84
    if index >= len(lst):
        return False
    num = lst[index]
    return 2 * num == sum((i for i in range(1, num) if num % i == 0))