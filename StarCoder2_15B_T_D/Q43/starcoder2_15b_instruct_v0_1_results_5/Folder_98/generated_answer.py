def find_primes_between_indices(lst):
    start_index = 1
    end_index = 2
    if start_index < 0 or end_index < 0 or end_index < start_index:
        return []
    primes = []
    for i in range(start_index, end_index + 1):
        is_prime = True
        for j in range(2, int(lst[i] ** 0.5) + 1):
            if lst[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(lst[i])
    primes.sort(reverse=True)
    return primes