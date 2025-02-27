def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for number in numbers[295:456]:
        if is_prime(number):
            primes.append(number)
    return sorted(primes, reverse=True)