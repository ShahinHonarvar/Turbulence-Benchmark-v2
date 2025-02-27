def is_perfect_num(num):
    return num == sum((divisor for divisor in range(1, num) if num % divisor == 0))

def if_perfect_num(num_list):
    return is_perfect_num(num_list[49]) if len(num_list) > 49 else False