def if_perfect_num(numbers_list):
    if len(numbers_list) > 4 and is_perfect(numbers_list[4]):
        return True
    return False

def is_perfect(num):
    sum_factors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_factors += i
            if i != num // i:
                sum_factors += num // i
    return sum_factors == num