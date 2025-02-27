from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[792]
    left_right_truncatable_primes = []

    def is_left_right_truncatable(n):
        str_n = str(n)
        while len(str_n) > 1:
            if '0' in str_n or not (isprime(int(str_n)) and isprime(int(str_n[1:])) and isprime(int(str_n[:-1]))):
                return False
            str_n = str_n[1:-1]
        return True
    for num in range(2, x + 1):
        if isprime(num) and is_left_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)