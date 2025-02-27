def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(my_tuple):
    x = my_tuple[803]
    right_truncatable_primes = []
    for i in range(2, x):
        is_right_truncatable = True
        for j in range(1, len(str(i))):
            truncated_num = int(str(i)[j:])
            if not is_prime(truncated_num):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)