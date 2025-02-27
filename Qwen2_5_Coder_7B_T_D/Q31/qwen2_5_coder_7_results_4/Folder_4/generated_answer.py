def if_perfect_num(num_list):
    if len(num_list) > 15:
        target_num = num_list[15]
        divisors = [i for i in range(1, target_num) if target_num % i == 0]
        return sum(divisors) == target_num
    else:
        return False