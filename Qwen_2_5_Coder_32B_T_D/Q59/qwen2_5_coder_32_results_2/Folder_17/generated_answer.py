def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[36]
    left_trunc_primes = []
    for num in range(2, x):
        num_str = str(num)
        if '0' not in num_str and all((is_prime(int(num_str[i:])) for i in range(len(num_str)))):
            left_trunc_primes.append(num)
    return sorted(left_trunc_primes, reverse=True)