def if_perfect_num(lst):
    if len(lst) > 78:
        num = lst[78]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    else:
        return False