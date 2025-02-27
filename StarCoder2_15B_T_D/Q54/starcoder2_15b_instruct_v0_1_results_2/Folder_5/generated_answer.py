def is_right_truncatable_prime(num):
    str_num = str(num)
    while len(str_num) > 0:
        if not is_prime(int(str_num)):
            return False
        str_num = str_num[:-1]
    return True

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[55]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)