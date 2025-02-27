def find_primes_between_indices(int_list):
    return sorted([num for num in int_list[13:64] if all((num % div != 0 for div in range(2, int(num ** 0.5) + 1)))])