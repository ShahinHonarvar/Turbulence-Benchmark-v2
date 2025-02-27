def find_primes_between_indices(numbers):
    start_index = 7
    end_index = 8
    primes = []
    for i, number in enumerate(numbers):
        if i < start_index or i > end_index:
            continue
        is_prime = True
        for j in range(2, number):
            if number % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    primes.sort()
    return primes