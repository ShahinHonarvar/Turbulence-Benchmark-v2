def all_left_truncatable_prime(tup):
    x = tup[4]
    truncatable_primes = []
    for i in range(2, x):
        is_truncatable_prime = True
        for j in range(1, len(str(i))):
            truncated_num = int(str(i)[j:])
            if not is_prime(truncated_num):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True