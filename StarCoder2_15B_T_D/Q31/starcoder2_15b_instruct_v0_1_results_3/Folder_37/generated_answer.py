def if_perfect_num(lst):
    return is_perfect_num(lst[28])

def is_perfect_num(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num