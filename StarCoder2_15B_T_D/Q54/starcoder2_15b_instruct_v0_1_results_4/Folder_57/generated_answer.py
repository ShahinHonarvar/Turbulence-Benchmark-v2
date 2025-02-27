import itertools

def all_right_truncatable_prime(numbers):
    x = numbers[54]
    right_truncatable_primes = []
    for i in range(1, len(str(x)) + 1):
        for permutation in itertools.permutations(str(x), i):
            number = int(''.join(permutation))
            if is_prime(number):
                right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True