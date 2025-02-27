def find_primes_between_indices(lst):
    return sorted([num for num in lst[229:851] if all((num % div != 0 for div in range(2, int(num ** 0.5) + 1)))], reverse=True)