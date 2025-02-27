def find_primes_between_indices(numbers):
    start, end = (56, 57)
    if start > end or end >= len(numbers):
        return []
    primes = [num for num in numbers[start:end + 1] if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and num > 1]
    return sorted(primes, reverse=True)