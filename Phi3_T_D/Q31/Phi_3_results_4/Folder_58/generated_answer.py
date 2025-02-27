def if_perfect_num(num_list):
    target_index = 714
    if target_index < len(num_list):
        n = num_list[target_index]
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    return False