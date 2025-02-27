def if_perfect_num(lst):

    def is_perfect_num(num):
        divisors = [x for x in range(1, int(num ** 0.5) + 1) if num % x == 0]
        return sum(divisors) == num
    return is_perfect_num(lst[64])