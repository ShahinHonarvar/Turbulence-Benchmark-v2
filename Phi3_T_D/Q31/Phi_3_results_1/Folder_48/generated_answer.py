def is_perfect_num(num):
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_divisors == num

def if_perfect_num(int_list):
    if 247 < len(int_list):
        return is_perfect_num(int_list[247])
    return False