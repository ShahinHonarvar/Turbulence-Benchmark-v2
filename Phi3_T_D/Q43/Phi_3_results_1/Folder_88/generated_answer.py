def find_primes_between_indices(int_list):
    result = []
    primes_in_range = [num for num in int_list[65:81 + 1] if all((num % div != 0 for div in range(2, int(num ** 0.5) + 1))) and num > 1]
    return sorted(primes_in_range)