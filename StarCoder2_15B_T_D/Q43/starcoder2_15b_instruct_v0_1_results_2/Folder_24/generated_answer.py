def find_primes_between_indices(numbers):
    primes = []
    for i, number in enumerate(numbers):
        is_prime = True
        if number > 1:
            for j in range(2, number):
                if number % j == 0:
                    is_prime = False
                    break
        else:
            is_prime = False
        if is_prime and 38 <= i <= 55:
            primes.append(number)
    primes.sort(reverse=True)
    return primes