def find_primes_between_indices(lst):
    primes = []
    for i in range(66, 82):
        num = lst[i]
        is_prime = True
        for j in range(2, num):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort()
    return primes