def find_primes_between_indices(numbers_list):

    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [number for number in numbers_list[12:63 + 1] if is_prime(number)]
    return sorted(primes)