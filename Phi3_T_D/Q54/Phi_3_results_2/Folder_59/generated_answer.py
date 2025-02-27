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
    x = numbers[84]
    right_truncatable_primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            digits = [int(d) for d in str(i)]
            if all((is_prime(int(''.join(map(str, digits[i:])))) for i in range(len(digits)))):
                right_truncatable_primes.append(i)
    return right_truncatable_primes[::-1]