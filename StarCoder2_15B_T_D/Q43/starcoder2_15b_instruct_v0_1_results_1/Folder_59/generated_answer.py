def find_primes_between_indices(number_list):
    primes = []
    for i, num in enumerate(number_list):
        if i < 5 or i > 8:
            continue
        is_prime = True
        for j in range(2, num):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True)