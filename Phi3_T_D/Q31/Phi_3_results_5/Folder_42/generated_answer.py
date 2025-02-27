def if_perfect_num(num_list):
    if len(num_list) > 276 and is_perfect(num_list[276]):
        return True
    return False

def is_perfect(num):
    sum_divisors, i = (0, 1)
    while i * i <= num:
        if num % i == 0:
            sum_divisors += i + (num // i if i != num // i else 0)
        i += 1
    return sum_divisors == num and num != 1