def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2 or (n != 2 and n % 2 == 0):
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0:
                return False
        return True
    result = []
    for index in range(23, 40):
        if is_prime(numbers[index]):
            result.append(numbers[index])
    return sorted(result)