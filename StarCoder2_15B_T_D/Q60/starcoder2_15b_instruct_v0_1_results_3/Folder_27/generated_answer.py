def all_left_right_truncatable_prime(x):
    x = x[79]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        is_left_right_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            left_truncation = int(str(i)[j:])
            right_truncation = int(str(i)[:-j - 1])
            if left_truncation < 2 or right_truncation < 2:
                continue
            if not is_prime(left_truncation) or not is_prime(right_truncation):
                is_left_right_truncatable_prime = False
                break
        if is_left_right_truncatable_prime:
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True