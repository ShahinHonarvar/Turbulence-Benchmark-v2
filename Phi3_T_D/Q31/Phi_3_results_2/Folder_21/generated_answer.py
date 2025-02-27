def if_perfect_num(int_list):
    if len(int_list) > 410 and is_perfect_number(int_list[410]):
        return True
    return False

def is_perfect_number(number):
    sum_of_divisors = 1
    i = 2
    while i * i <= number:
        if number % i == 0:
            sum_of_divisors += i + number // i
        if i == number // i:
            break
        i += 1
    return sum_of_divisors == number