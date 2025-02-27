def find_primes_between_indices(numbers):
    primes = []
    for number in numbers[61:80]:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    primes.sort()
    return primes