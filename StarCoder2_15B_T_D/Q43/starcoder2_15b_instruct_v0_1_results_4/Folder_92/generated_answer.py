def find_primes_between_indices(nums):
    start_index = 7
    end_index = 8
    primes = []
    for i, num in enumerate(nums):
        if start_index <= i <= end_index:
            is_prime = True
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    primes.sort()
    return primes