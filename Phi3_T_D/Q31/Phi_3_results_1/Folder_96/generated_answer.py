def if_perfect_num(list_of_numbers):
    if len(list_of_numbers) > 47:
        number_at_index_47 = list_of_numbers[47]
        if is_perfect_number(number_at_index_47):
            return True
        else:
            return False
    return False

def is_perfect_number(n):
    sum_of_divisors = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:
                sum_of_divisors += n // i
        i += 1
    return sum_of_divisors == n and n != 1