def find_primes_between_indices(numbers):
    primes = []
    for i in range(35, 90):
        num = numbers[i]
        is_prime = True
        for j in range(2, num):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort(reverse=True)
    return primes