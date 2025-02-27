def is_prime(n):
    if n <= 1:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        p += 1
    return True

def all_right_truncatable_prime(tup):
    x = tup[54]
    truncatable_primes = []
    for num in range(23, x):
        original_num = num
        prime = True
        while num > 0:
            if not is_prime(num):
                prime = False
                break
            num = int(str(num)[:-1])
        if prime and is_prime(original_num):
            truncatable_primes.append(original_num)
    return sorted(truncatable_primes)