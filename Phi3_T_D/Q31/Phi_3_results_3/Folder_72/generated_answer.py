def is_perfect_num(num):
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_divisors == num

def if_perfect_num(num_list):
    return is_perfect_num(num_list[16]) if len(num_list) > 16 else False