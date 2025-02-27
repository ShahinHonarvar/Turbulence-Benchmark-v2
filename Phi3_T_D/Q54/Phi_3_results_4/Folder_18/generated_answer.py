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

def all_right_truncatable_prime(numbers):
    x = numbers[429]
    right_truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            digits = list(str(i))
            while len(digits) > 1:
                if not is_prime(int(''.join(digits))):
                    break
                digits.pop()
            else:
                right_truncatable_primes.append(i)
    return right_truncatable_primes