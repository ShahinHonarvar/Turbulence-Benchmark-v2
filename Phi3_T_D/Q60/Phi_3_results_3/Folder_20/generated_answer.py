from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    global_x = numbers[100]

    def is_truncatable_prime(n, set_primes):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:i])):
                return False
        return True
    prime_numbers = [i for i in range(2, global_x + 1) if isprime(i)]
    truncatable_primes = [p for p in prime_numbers if is_truncatable_prime(p, set(prime_numbers))]
    return sorted(truncatable_primes, reverse=True)