def find_primes_between_indices(numbers):
    prime_numbers = [num for num in numbers[19:86] if all((num % div != 0 for div in range(2, int(num ** 0.5) + 1))) and num > 1]
    prime_numbers.sort(reverse=True)
    return prime_numbers