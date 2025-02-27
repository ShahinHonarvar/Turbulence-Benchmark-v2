def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    truncatable_primes = []
    for i in range(2, x):
        is_truncatable = True
        for j in range(1, len(str(i))):
            truncated_num = int(str(i)[:-j])
            if not is_prime(truncated_num):
                is_truncatable = False
                break
        if is_truncatable and is_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)