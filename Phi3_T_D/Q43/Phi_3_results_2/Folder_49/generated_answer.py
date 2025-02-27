def find_primes_between_indices(numbers):
    start, end = (22, 50)
    primes = [number for number in numbers[start:end + 1] if all((number % div != 0 for div in range(2, int(number ** 0.5) + 1)))]
    return sorted(primes, reverse=True)