def is_prime(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return False

def all_left_truncatable_prime(tup):
    if 32 in tup:
        x = tup[32]
        if is_prime(x):
            left_truncatable_primes = []
            for i in range(2, x):
                num = i
                while num > 0:
                    if is_prime(num):
                        left_truncatable_primes.append(i)
                        break
                    num //= 10
            return sorted(left_truncatable_primes)
    return []