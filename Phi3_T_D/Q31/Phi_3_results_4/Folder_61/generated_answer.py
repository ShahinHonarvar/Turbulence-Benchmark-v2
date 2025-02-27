def if_perfect_num(num_list):
    if len(num_list) < 9:
        return False
    perfect_num = num_list[8]
    divisors = [i for i in range(1, perfect_num) if perfect_num % i == 0]
    return sum(divisors) == perfect_num