from itertools import product

def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def all_combinations(prefix, length):
        if length == 1:
            return [str(prime) for prime in primes if str(prime).startswith(prefix)]
        return [combo for combo in product(digits, repeat=length - 1) for prime in all_combinations(prefix + str(combo[0]), length - 1)]
    x = numbers[14]
    primes = [11, 13, 17, 31, 37, 71, 73, 79, 97]
    digits = '1379'
    truncatable_primes = set()
    for length in range(1, len(str(x)) + 1):
        for combo in all_combinations('', length):
            candidates = [combo + digit for digit in digits]
            for num in candidates:
                if num > x:
                    break
                if is_prime(int(num)):
                    truncatable_primes.add(int(num))
    return sorted(list(truncatable_primes))