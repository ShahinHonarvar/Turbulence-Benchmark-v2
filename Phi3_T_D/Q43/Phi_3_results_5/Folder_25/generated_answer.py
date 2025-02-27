def find_primes_between_indices(list_of_ints):
    start, end = (53, 54)
    prime_numbers = [x for x in list_of_ints[start:end + 1] if all((x % i != 0 for i in range(2, x))) and x > 1]
    return sorted(prime_numbers)