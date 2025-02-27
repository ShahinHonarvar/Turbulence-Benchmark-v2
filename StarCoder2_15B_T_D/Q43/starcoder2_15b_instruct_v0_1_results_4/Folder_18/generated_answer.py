def find_primes_between_indices(numbers):
    start_index = 430
    end_index = 805
    primes = []
    for i, number in enumerate(numbers):
        if i < start_index:
            continue
        if i > end_index:
            break
        is_prime = True
        for j in range(2, number):
            if number % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    primes.sort()
    return primes