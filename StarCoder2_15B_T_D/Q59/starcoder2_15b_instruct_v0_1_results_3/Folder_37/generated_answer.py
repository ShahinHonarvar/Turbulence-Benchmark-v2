def all_left_truncatable_prime(args):
    x = args[0]
    left_truncatable_primes = []
    for i in range(2, x):
        is_left_truncatable = True
        temp = i
        while temp > 0:
            digit = temp % 10
            if digit == 0 or not is_prime(temp):
                is_left_truncatable = False
                break
            temp //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True