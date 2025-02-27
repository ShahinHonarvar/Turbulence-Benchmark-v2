def find_primes_between_indices(numbers):
    start_index, end_index = (38, 55)
    primes_in_range = [num for num in numbers[start_index:end_index + 1] if all((num % div != 0 for div in range(2, int(num ** 0.5) + 1)))]
    return sorted(primes_in_range, reverse=True)