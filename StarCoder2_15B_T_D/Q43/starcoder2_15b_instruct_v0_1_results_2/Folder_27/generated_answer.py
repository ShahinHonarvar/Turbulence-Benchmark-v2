def find_primes_between_indices(nums):
    start_index = 11
    end_index = 11
    primes = []
    for i, num in enumerate(nums):
        if i < start_index:
            continue
        if i > end_index:
            break
        if num > 1:
            is_prime = True
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    primes.sort()
    return primes