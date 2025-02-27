from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[67]
    right_trunc_primes = []

    def check_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    for num in range(2, x):
        if check_right_truncatable(num):
            right_trunc_primes.append(num)
    return sorted(right_trunc_primes, reverse=True)