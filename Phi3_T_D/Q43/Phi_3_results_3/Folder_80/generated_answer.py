def find_primes_between_indices(numbers):
    return sorted((num for num in numbers[12:30] if all((num % i for i in range(2, int(num ** 0.5) + 1)))), reverse=True)