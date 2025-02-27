def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = [num for num in numbers[87:90] if is_prime(num)]
    return sorted(primes)