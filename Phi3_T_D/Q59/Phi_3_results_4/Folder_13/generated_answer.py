def generate_primes(up_to):
    sieve = [True] * (up_to + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(up_to ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, up_to + 1, i):
                sieve[j] = False
    return [number for number, is_prime in enumerate(sieve) if is_prime]

def is_left_truncatable_prime(number, primes):
    str_number = str(number)
    for i in range(len(str_number)):
        if int(str_number[i:]) not in primes:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[784]
    primes = generate_primes(x - 1)
    left_truncatable_primes = []
    for prime in primes:
        if is_left_truncatable_prime(prime, primes):
            left_truncatable_primes.append(prime)
    return left_truncatable_primes