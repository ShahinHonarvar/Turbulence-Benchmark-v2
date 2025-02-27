def find_primes_between_indices(num_list):
    primes = []
    for i, num in enumerate(num_list):
        if i < 69:
            continue
        elif i > 80:
            break
        is_prime = True
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort()
    return primes