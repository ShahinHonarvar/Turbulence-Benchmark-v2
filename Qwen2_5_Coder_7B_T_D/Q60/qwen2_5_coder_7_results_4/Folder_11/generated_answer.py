from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    left_right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if '0' in str_prime:
            continue
        is_left_right_truncatable = True
        for i in range(len(str_prime)):
            if not (isprime(int(str_prime[i:])) and isprime(int(str_prime[:len(str_prime) - i]))):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes)