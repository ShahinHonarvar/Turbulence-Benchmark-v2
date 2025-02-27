def all_left_right_truncatable_prime(t):
    x = t[49]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        is_left_right_truncatable = True
        for j in range(len(str(i)) - 1):
            truncated_number = int(str(i)[j + 1:])
            if not is_prime(truncated_number):
                is_left_right_truncatable = False
                break
            truncated_number = int(str(i)[:-j - 1])
            if not is_prime(truncated_number):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True