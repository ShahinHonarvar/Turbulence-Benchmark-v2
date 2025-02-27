def if_perfect_num(num_list):
    index = 92
    if index >= len(num_list):
        return False
    return is_perfect_number(num_list[index])

def is_perfect_number(num):
    sum_of_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
    return sum_of_divisors == num