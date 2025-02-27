def all_left_right_truncatable_prime(tuple_of_positive_integers):
    left_right_truncatable_primes = []
    for num in tuple_of_positive_integers:
        if is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes

def is_left_right_truncatable_prime(num):
    if num < 10:
        return is_prime(num)
    if num % 10 == 0:
        return False
    if not is_prime(num):
        return False
    return is_left_right_truncatable_prime(num // 10)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True