def find_primes_between_indices(num_list):
    return sorted([num for num in num_list[52:54] if all((num % n != 0 for n in range(2, int(num ** 0.5) + 1)))])