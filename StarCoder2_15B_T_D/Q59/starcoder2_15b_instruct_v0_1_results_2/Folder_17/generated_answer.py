def all_left_truncatable_prime(tup):
    x = tup[36]
    truncatable_primes = []
    for i in range(2, x):
        is_truncatable = True
        for j in range(len(str(i)) - 1):
            substring = str(i)[j + 1:]
            if int(substring) < 2 or not is_prime(int(substring)):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True