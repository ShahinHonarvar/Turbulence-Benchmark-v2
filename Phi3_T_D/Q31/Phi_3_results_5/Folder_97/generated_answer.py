def is_perfect_num(num):
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

def if_perfect_num(integers):
    return is_perfect_num(integers[132]) if len(integers) > 132 else False