def find_primes_between_indices(int_list):
    primes = []
    for i, num in enumerate(int_list):
        if i >= 33 and i <= 35:
            is_prime = True
            for j in range(2, num // 2 + 1):
                if num % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    primes.sort()
    return primes