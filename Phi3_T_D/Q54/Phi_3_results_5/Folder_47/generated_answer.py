def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_right_truncatable_primes(n):
    right_truncatable_primes = []
    a = 2
    while a < n:
        if is_prime(a):
            temp = a
            b = a
            while b % 10 != 0:
                if is_prime(b):
                    right_truncatable_primes.append(b)
                b //= 10
            if b == a:
                right_truncatable_primes.append(a)
        a += 1
    return right_truncatable_primes

def all_right_truncatable_prime(numbers):
    x = numbers[49]
    return sorted(find_right_truncatable_primes(x))