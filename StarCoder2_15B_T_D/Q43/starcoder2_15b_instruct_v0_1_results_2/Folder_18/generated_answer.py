def find_primes_between_indices(numbers):
    primes = []
    for num in numbers[430:806]:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort()
    return primes