def all_left_truncatable_prime(x):
    prime_numbers = generate_prime_numbers(x[79])
    left_truncatable_prime_numbers = filter(is_left_truncatable_prime, prime_numbers)
    return sorted(left_truncatable_prime_numbers, reverse=True)

def is_left_truncatable_prime(number):
    while number > 0:
        if not is_prime(number):
            return False
        number //= 10
    return True

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_prime_numbers(x):
    is_prime = [True] * x
    for i in range(2, int(x ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, x, i):
                is_prime[j] = False
    return [i for i in range(2, x) if is_prime[i]]