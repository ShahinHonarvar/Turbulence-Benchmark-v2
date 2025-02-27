def if_perfect_num(lst):

    def check_perfect(n):
        sum_of_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_of_divisors += i
        return sum_of_divisors == n
    return check_perfect(lst[714])