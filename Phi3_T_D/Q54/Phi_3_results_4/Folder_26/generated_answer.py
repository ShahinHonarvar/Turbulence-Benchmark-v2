from sympy import isprime

def all_right_truncatable_prime(numbers):
    right_truncatable_primes = []
    x = numbers[81]

    def is_right_truncatable(n):
        for i in range(len(str(n))):
            if not isprime(int(str(n)[:-1])):
                return False
            n = int(str(n)[:-1])
        return True
    for number in range(x - 1, 10, -1):
        if all((isprime(digit) for digit in map(int, str(number)))) and is_right_truncatable(number):
            right_truncatable_primes.append(number)
    return right_truncatable_primes