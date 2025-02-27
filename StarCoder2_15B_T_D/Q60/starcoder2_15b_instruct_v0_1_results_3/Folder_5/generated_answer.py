def is_truncatable_prime(n):
    if n < 10:
        return n in (2, 3, 5, 7)
    s = str(n)
    return all((int(s[i:]) in primes for i in range(len(s)))) and all((int(s[:-i]) in primes for i in range(1, len(s))))

def all_left_right_truncatable_prime(t):
    x = t[55]
    primes = [i for i in range(2, x + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    return sorted(filter(is_truncatable_prime, primes))