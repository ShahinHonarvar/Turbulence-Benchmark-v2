def is_perfect_num(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    if sum(divisors) == num:
        return True
    else:
        return False

def if_perfect_num(num_list):
    return is_perfect_num(num_list[990]) if len(num_list) > 990 else False