def all_right_truncatable_prime(input_tuple):
    x = input_tuple[18]
    right_truncatable_primes = []
    for i in range(2, x):
        is_right_truncatable = True
        temp = i
        while temp > 0:
            if not is_prime(temp):
                is_right_truncatable = False
                break
            temp //= 10
        if is_right_truncatable:
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True