def find_primes_between_indices(numbers):
    start, end = (112, 361)
    primes = [num for num in numbers[start - 1:end] if all((num % div != 0 for div in range(2, int(num ** 0.5) + 1)))]
    return sorted(primes, reverse=True)