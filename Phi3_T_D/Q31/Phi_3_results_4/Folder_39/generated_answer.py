def if_perfect_num(int_list):
    if len(int_list) > 59 and (not is_perfect(int_list[59])):
        return False
    return True

def is_perfect(num):
    sum_of_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
    return num == sum_of_divisors