def find_primes_between_indices(numbers):
    start, end = (14, 73)
    primes = [num for num in numbers[start:end + 1] if all((num % div != 0 for div in range(2, int(num ** 0.5) + 1))) and num > 1]
    return sorted(primes, reverse=True)