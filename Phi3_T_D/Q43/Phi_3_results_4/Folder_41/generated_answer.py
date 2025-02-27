def find_primes_between_indices(numbers):
    start, end = (45, 80)
    primes = [num for idx, num in enumerate(numbers[start:end + 1]) if all((num % div != 0 for div in range(2, int(num ** 0.5) + 1))) and num > 1]
    return sorted(primes, reverse=True)