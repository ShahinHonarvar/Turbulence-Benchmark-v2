def find_primes_between_indices(nums):
    start_index = 43
    end_index = 76
    primes = []
    for i, num in enumerate(nums):
        if start_index <= i <= end_index:
            is_prime = True
            for j in range(2, num // 2 + 1):
                if num % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    primes.sort(reverse=True)
    return primes