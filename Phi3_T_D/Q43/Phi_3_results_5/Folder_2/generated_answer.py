def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    start_index = 167
    end_index = 785
    primes_in_range = [num for i, num in enumerate(numbers[start_index:end_index + 1]) if is_prime(num)]
    return sorted(primes_in_range, reverse=True)