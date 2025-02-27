def find_primes_between_indices(numbers):
    start_index = 149
    end_index = 979
    primes = []
    for i in range(start_index, end_index + 1):
        number = numbers[i]
        is_prime = True
        for j in range(2, number):
            if number % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    primes.sort()
    return primes