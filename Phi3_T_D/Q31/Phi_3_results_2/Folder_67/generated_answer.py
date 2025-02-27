def is_perfect_num(num):
    if num < 1:
        return False
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

def if_perfect_num(num_list):
    try:
        return is_perfect_num(num_list[43])
    except IndexError:
        return False