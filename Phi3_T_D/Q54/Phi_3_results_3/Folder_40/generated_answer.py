def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes_set):
    n_str = str(n)
    for i in range(len(n_str)):
        if not is_prime(int(n_str[i:])):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[10]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []
    for num in reversed(range(2, x)):
        if is_prime(num) and num > 10 and is_right_truncatable_prime(num, primes):
            right_truncatable_primes.append(num)
    return right_truncatable_primes