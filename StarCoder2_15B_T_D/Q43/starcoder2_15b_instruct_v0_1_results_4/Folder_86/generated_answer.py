def find_primes_between_indices(nums):
    primes = []
    for i, num in enumerate(nums):
        is_prime = True
        for j in range(2, num):
            if num % j == 0:
                is_prime = False
                break
        if is_prime and i >= 459 and (i <= 781):
            primes.append(num)
    primes.sort()
    return primes