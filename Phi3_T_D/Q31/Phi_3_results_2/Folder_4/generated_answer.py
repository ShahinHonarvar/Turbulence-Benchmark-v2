def is_perfect_num(num_list):
    if 15 >= len(num_list):
        return False

    def sum_of_divisors(n):
        return sum((i for i in range(1, n) if n % i == 0))
    return sum_of_divisors(num_list[15]) == num_list[15]