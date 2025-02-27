def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(46, 62):
        num = numbers[i]
        is_prime = True
        for j in range(2, num):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    prime_numbers.sort()
    return prime_numbers