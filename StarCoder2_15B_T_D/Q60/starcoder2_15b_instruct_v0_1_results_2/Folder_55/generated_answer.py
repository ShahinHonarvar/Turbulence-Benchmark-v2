def is_truncatable_prime(number):
    if number < 10:
        return number in (2, 3, 5, 7)
    return is_truncatable_prime(int(str(number)[1:])) and is_truncatable_prime(int(str(number)[:-1])) and (number % 2 != 0) and (number % 3 != 0) and (number % 5 != 0) and (number % 7 != 0)

def generate_truncatable_primes(x):
    truncatable_primes = []
    for number in range(2, x + 1):
        if is_truncatable_prime(number):
            truncatable_primes.append(number)
    return truncatable_primes

def all_left_right_truncatable_prime(t):
    x = t[73]
    truncatable_primes = generate_truncatable_primes(x)
    return sorted(truncatable_primes, reverse=True)