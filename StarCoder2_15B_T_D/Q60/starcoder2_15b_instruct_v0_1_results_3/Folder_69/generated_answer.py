def all_left_right_truncatable_prime(numbers):
    x = numbers[760]
    truncatable_primes = []
    for n in range(2, x + 1):
        is_truncatable = True
        for i in range(1, len(str(n))):
            left_trunc = int(str(n)[i:])
            right_trunc = int(str(n)[:-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(n)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True