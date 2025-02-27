def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    left_right_truncatable_primes = []
    for i in range(11, x + 1):
        if is_prime(i):
            if is_left_right_truncatable_prime(i):
                left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    if num < 10:
        return is_prime(num)
    if num % 10 == 0:
        return False
    if not is_prime(num):
        return False
    return is_left_right_truncatable_prime(num // 10)