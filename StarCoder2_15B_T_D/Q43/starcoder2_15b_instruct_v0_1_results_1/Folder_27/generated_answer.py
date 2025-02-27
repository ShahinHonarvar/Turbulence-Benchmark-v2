def find_primes_between_indices(nums):
    """
    Finds the sorted list of all prime numbers from index 11 to index 11, both inclusive.
    If no prime number exists in the specified range, returns an empty list.
    """
    primes = [x for x in range(2, 100) if all((x % y != 0 for y in range(2, x)))]
    return [x for x in primes if 11 <= nums.index(x) <= 11]