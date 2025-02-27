def find_primes_between_indices(numbers):

    def is_prime(num):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        return False
    primes = []
    if len(numbers) > 8:
        for number in numbers[7:9]:
            if is_prime(number):
                primes.append(number)
    return sorted(primes)