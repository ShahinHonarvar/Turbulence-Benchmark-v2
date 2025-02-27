def find_primes_between_indices(lst):
    start, end = (30, 43)
    primes = [num for num in lst[start:end + 1] if all((num % div != 0 for div in range(2, int(num ** 0.5) + 1))) and num > 1]
    return sorted(primes)