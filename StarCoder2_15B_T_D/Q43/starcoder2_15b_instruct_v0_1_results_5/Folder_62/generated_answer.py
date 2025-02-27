import primes

def find_primes_between_indices(nums):
    """
    Finds all prime numbers in the specified range.
    Args:
        nums (list): A list of integers.
    Returns:
        list: A sorted list of prime numbers from index 29 to index 97, both inclusive.
    """
    start_index = 29
    end_index = 97
    return sorted(primes.primes_between(start_index, end_index), reverse=True)