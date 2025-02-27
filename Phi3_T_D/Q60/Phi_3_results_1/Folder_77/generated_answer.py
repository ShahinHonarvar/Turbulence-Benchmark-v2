def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[767]
    primes = [int(str(i)[::-1]) for i in range(23, x + 1) if is_prime(i)]
    left_right_primes = []
    seen = set()
    for prime in primes:
        if prime in seen or not is_prime(int(str(prime)[::-1])):
            continue
        seen.add(prime)
        is_truncatable = True
        if str(prime)[1:] == '0' or int(str(prime)[1:]) not in primes:
            is_truncatable = False
        if is_truncatable:
            left_right_primes.append(prime)
    return sorted(left_right_primes, reverse=True)