def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[645]
    truncable_primes = []
    for num in range(2, x):
        if is_prime(num):
            digits = str(num)
            prime = True
            while len(digits) > 1 and prime:
                digits = digits[:-1]
                prime = is_prime(int(digits))
            if prime and digits:
                truncable_primes.append(int(digits))
    return sorted(truncable_primes)