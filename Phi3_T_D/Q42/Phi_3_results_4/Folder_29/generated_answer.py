def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    prime_factors_set = set()
    num_to_factor = numbers[19]
    i = 2
    while i * i <= num_to_factor:
        if num_to_factor % i:
            i += 1
        else:
            num_to_factor //= i
            prime_factors_set.add(i)
    if num_to_factor > 1:
        prime_factors_set.add(num_to_factor)
    return prime_factors_set