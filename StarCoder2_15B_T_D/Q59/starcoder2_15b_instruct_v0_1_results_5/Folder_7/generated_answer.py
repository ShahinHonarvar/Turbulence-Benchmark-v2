def all_left_truncatable_prime(input_tuple):
    x = input_tuple[803]
    left_truncatable_primes = [2, 3, 5, 7]
    for i in range(10):
        new_primes = []
        for prime in left_truncatable_primes:
            for j in range(10):
                new_number = prime * 10 + j
                if is_prime(new_number):
                    new_primes.append(new_number)
        left_truncatable_primes = new_primes
    return sorted(left_truncatable_primes)

def is_prime(number):
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(number ** 0.5) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True