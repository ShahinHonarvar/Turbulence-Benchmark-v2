def if_perfect_num(num_list):

    def is_perfect_num(num):
        divisors = [d for d in range(1, num) if num % d == 0]
        return sum(divisors) == num
    return is_perfect_num(num_list[94])