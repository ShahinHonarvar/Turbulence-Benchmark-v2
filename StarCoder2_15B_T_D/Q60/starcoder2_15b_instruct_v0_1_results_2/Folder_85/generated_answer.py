def all_left_right_truncatable_prime(tup):
    x = tup[94]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        is_left_right_truncatable_prime = True
        for digits in range(1, len(str(num))):
            left_truncation = int(str(num)[digits:])
            right_truncation = int(str(num)[:-digits])
            if not (is_prime(left_truncation) and is_prime(right_truncation)):
                is_left_right_truncatable_prime = False
                break
        if is_left_right_truncatable_prime:
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True