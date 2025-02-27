def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_right_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    while len(str_num) > 1:
        if not is_prime(int(str_num)):
            return False
        str_num = str_num[1:-1]
    return is_prime(int(str_num))

def all_left_right_truncatable_prime(tup):
    x = tup[3]
    primes = [num for num in range(2, x + 1) if is_prime(num)]
    return sorted([num for num in primes if is_left_right_truncatable_prime(num)], reverse=True)