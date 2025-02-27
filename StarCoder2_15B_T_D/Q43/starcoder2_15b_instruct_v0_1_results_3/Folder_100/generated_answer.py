def find_primes_between_indices(numbers):
    result = []
    for number in numbers[25:63]:
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            result.append(number)
    result.sort()
    return result