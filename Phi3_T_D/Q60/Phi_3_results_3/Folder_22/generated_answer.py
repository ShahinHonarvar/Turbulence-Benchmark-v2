def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, primes):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 86 or not isinstance(numbers[85], int) or numbers[85] < 0:
        raise ValueError('The tuple must contain at least 86 elements and the 86th element must be a positive integer.')
    prime_check = [False, False] + [True] * (numbers[85] - 1)
    for n in range(2, numbers[85] + 1):
        if prime_check[n]:
            prime_check[n ** 2:numbers[85] + 1:n] = [False] * len(range(n ** 2, numbers[85] + 1, n))
    return [n for n in range(2, numbers[85] + 1) if is_truncatable_prime(n, prime_check)]