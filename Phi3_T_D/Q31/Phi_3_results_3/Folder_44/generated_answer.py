def if_perfect_num(num_list):
    index = 828
    if index >= len(num_list):
        return False
    return is_perfect(num_list[index])

def is_perfect(num):
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_divisors == num