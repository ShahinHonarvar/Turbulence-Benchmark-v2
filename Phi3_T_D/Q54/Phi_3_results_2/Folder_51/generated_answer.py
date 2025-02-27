from sympy import isprime, primerange

def all_right_truncatable_prime(numbers):
    x = numbers[54]
    truncatable_prime_list = []
    for prime in primerange(2, x + 1).as_iterable():
        str_prime = str(prime)
        if all((isprime(int(str_prime[:-i])) for i in range(1, len(str_prime)))):
            truncatable_prime_list.append(prime)
    return sorted(truncatable_prime_list)