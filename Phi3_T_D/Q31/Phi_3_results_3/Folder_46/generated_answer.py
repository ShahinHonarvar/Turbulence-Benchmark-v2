def is_perfect_num(num):
    if num < 1:
        return False
    sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_of_divisors == num

def if_perfect_num(num_list):
    if len(num_list) > 453:
        return is_perfect_num(num_list[453])
    else:
        return False