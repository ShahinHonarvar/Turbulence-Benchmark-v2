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

def right_truncatable_primes(limit):
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            str_num = str(num)
            while str_num:
                if not is_prime(int(str_num)):
                    break
                str_num = str_num[:-1]
            else:
                primes.append(num)
    return sorted(primes, reverse=True)

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[39]
    return right_truncatable_primes(x)