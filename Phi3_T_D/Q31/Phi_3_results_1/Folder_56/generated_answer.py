def if_perfect_num(num_list):
    return sum_of_divisors(num_list[60]) == num_list[60]

def sum_of_divisors(n):
    sum_divisors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors