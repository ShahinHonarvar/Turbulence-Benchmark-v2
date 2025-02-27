def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[43]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        temp = i
        while temp > 9:
            temp //= 10
            if not is_prime(temp):
                is_truncatable = False
                break
        temp = i
        while temp > 9:
            temp %= 10 ** (len(str(temp)) - 1)
            if not is_prime(temp):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)

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