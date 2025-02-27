def find_primes_between_indices(numbers):
    """
    Find all prime numbers from index 31 to index 67, both inclusive, in the given list of
    integers and sort them in descending order. If no prime number exists in the specified range,
    return an empty list.

    :param numbers: A list of integers.
    :return: A sorted list of prime numbers from index 31 to index 67, both inclusive, in
        descending order. If no prime number exists in the specified range, return an empty list.
    """

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [n for i, n in enumerate(numbers) if 31 <= i <= 67 and is_prime(n)]
    primes.sort(reverse=True)
    return primes