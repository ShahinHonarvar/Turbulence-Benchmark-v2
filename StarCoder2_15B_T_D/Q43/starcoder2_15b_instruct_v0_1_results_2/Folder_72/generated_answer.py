def find_primes_between_indices(input_list):
    primes = []
    for i in range(28, 45):
        num = input_list[i]
        is_prime = True
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes)