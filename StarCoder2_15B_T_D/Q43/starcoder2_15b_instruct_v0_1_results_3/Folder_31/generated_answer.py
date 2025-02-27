def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = []
    for index, number in enumerate(numbers):
        if is_prime(number) and 37 <= index <= 95:
            primes.append(number)
    return sorted(primes, reverse=True)