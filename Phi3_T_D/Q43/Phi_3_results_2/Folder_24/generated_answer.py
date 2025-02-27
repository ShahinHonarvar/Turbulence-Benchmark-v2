def find_primes_between_indices(numbers):
    prime_list = [num for num in numbers[37:55] if all((num % div != 0 for div in range(2, int(num ** 0.5) + 1))) and num > 1]
    return sorted(prime_list, reverse=True)