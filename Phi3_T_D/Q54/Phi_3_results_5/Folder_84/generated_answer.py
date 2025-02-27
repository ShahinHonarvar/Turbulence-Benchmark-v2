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

def all_right_truncatable_prime(int_tuple):
    threshold = int_tuple[630]
    right_truncatable_primes = []
    for i in range(threshold, 1, -1):
        if is_prime(i):
            is_truncatable = True
            num_str = str(i)
            while num_str:
                num_str = num_str[:-1]
                if not is_prime(int(num_str)):
                    is_truncatable = False
                    break
            if is_truncatable:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)