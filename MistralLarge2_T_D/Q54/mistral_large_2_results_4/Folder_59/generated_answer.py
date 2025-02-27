def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[84]
    primes = []

    def is_right_truncatable_prime(num):
        num_str = str(num)
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[:-1]
        return True
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)