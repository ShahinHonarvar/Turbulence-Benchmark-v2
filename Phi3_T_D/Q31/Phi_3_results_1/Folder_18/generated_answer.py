def is_perfect_num(num):
    sum_of_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
    return sum_of_divisors == num

def if_perfect_num(list_of_ints):
    if len(list_of_ints) > 312 and list_of_ints[312] > 0:
        return is_perfect_num(list_of_ints[312])
    return False