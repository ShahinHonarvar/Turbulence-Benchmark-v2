def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[26]
    trunc_primes = []
    for num in range(23, x):
        if is_prime(num):
            is_truncatable = True
            temp_num = num
            while is_truncatable and temp_num > 0:
                temp_num = int(str(temp_num)[:-1])
                if not is_prime(temp_num):
                    is_truncatable = False
            if is_truncatable:
                trunc_primes.append(num)
    return sorted(trunc_primes)