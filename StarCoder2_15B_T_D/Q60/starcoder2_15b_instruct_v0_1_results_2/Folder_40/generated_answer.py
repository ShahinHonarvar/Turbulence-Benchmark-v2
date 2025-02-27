def all_left_right_truncatable_prime(x: tuple) -> list:
    x = x[0]
    left_right_truncatable_primes = []
    for i in range(11, x + 1):
        is_left_right_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            left_truncation = int(str(i)[j:])
            right_truncation = int(str(i)[:-j - 1])
            if not is_prime(left_truncation) or not is_prime(right_truncation):
                is_left_right_truncatable_prime = False
                break
        if is_left_right_truncatable_prime:
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True