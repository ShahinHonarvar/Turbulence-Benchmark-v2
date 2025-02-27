def if_perfect_num(int_list):
    if 985 < len(int_list):
        n = int_list[985]
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    return False