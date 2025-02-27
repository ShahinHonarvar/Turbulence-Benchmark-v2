def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[77]
    truncatable_primes = []
    primes = {2, 3, 5, 7}
    for number in range(x, 1, -1):
        s = str(number)
        if s.startswith('0') or any((int(s[i:]) not in primes for i in range(1, len(s)))):
            continue
        primes |= {int(s[i:]) for i in range(1, len(s))}
        truncatable_primes.append(number)
    return truncatable_primes