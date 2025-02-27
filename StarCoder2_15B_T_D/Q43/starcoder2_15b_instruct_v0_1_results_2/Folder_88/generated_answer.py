def find_primes_between_indices(numbers):
    start_index = 66
    end_index = 81
    primes = []
    for number in numbers[start_index:end_index + 1]:
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    primes.sort()
    return primes