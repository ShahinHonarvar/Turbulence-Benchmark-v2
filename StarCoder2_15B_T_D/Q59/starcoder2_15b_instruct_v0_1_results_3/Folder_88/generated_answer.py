from itertools import permutations

def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[93]
    left_truncatable_primes = []
    for i in range(1, len(str(x)) + 1):
        for permutation in permutations(str(x), i):
            number = int(''.join(permutation))
            if is_prime(number) and number not in left_truncatable_primes:
                left_truncatable_primes.append(number)
    left_truncatable_primes.sort()
    return left_truncatable_primes