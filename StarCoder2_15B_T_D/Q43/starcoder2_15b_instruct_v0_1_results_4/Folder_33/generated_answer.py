def find_primes_between_indices(nums):
    primes = []
    for i, num in enumerate(nums):
        is_prime = True
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime and 289 <= i <= 381:
            primes.append(num)
    primes.sort(reverse=True)
    return primes