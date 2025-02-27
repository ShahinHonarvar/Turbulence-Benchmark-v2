def if_perfect_num(lst):

    def is_perfect(num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    return is_perfect(lst[48]) if len(lst) > 48 else False