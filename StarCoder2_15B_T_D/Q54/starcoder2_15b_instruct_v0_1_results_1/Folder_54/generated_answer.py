import itertools

def all_right_truncatable_prime(numbers):
    x = numbers[88]
    right_truncatable_primes = []
    for i in range(1, len(str(x))):
        for permutation in itertools.permutations(str(x), i):
            number = int(''.join(permutation))
            if is_prime(number):
                right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True