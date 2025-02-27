def if_perfect_num(num_list):
    if len(num_list) > 34 and is_perfect(num_list[34]):
        return True
    return False

def is_perfect(num):
    sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_of_divisors == num