from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[88]

    def is_left_right_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if '0' in str(n) or not isprime(int(n_str[i:])) or (not isprime(int(n_str[:len(n_str) - i]))):
                return False
        return True
    primes = [i for i in range(2, x + 1) if isprime(i) and is_left_right_truncatable(i)]
    return sorted(primes, reverse=True)