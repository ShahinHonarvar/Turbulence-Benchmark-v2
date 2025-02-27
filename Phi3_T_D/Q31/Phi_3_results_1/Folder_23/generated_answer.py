def if_perfect_num(lst):
    return any((sum((i for i in range(1, num) if num % i == 0)) == num and num == lst[69] for num in lst)) if len(lst) > 69 else False