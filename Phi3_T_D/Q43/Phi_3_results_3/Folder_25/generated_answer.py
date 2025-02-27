def find_primes_between_indices(list_of_integers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_numbers = []
    for i in range(52, 54):
        if is_prime(list_of_integers[i]):
            prime_numbers.append(list_of_integers[i])
    return sorted(prime_numbers)