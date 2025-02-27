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

def all_left_right_truncatable_prime(numbers):
    x = numbers[39] if len(numbers) > 39 else 0
    results = []
    primes = [str(i) for i in range(2, x + 1) if is_prime(i)]
    for prime_str in primes:
        if not any((digit in str(prime_str) for digit in '0468')):
            valid = True
            while prime_str:
                if not is_prime(int(prime_str)) or any((digit in str(prime_str) for digit in '0468')):
                    valid = False
                    break
                prime_str = prime_str[1:-1]
            if valid:
                results.append(int(prime_str))
    return results