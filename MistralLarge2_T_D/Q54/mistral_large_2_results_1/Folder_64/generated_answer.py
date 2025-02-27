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

def all_right_truncatable_prime(tup):
    x = tup[4]
    primes = []
    for num in range(2, x):
        temp_num = num
        while temp_num > 0:
            if not is_prime(temp_num):
                break
            temp_num //= 10
        else:
            primes.append(num)
    return sorted(primes)