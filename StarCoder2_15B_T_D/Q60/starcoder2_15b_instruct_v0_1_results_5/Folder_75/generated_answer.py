def is_left_right_truncatable_prime(n):
    while n >= 10:
        if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or (n % 7 == 0):
            return False
        n = int(str(n)[1:])
        n = int(str(n)[:-1])
    if n == 2 or n == 3 or n == 5 or (n == 7):
        return True
    else:
        return False

def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for n in numbers:
        if is_left_right_truncatable_prime(n):
            left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes)