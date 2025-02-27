def is_left_right_truncatable_prime(n):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if not is_prime(n):
        return False
    if n < 10:
        return is_prime(n)
    return is_left_right_truncatable_prime(int(str(n)[1:])) and is_left_right_truncatable_prime(int(str(n)[:-1]))

def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for n in numbers:
        if is_left_right_truncatable_prime(n):
            left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes)