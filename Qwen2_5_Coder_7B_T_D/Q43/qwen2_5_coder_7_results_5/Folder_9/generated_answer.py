def find_primes_between_indices(lst):
    return sorted([num for num in lst[16:72] if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and num > 1])