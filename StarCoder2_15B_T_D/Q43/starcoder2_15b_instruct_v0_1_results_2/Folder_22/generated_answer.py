def find_primes_between_indices(input_list):
    start_index = 75
    end_index = 85
    primes = []
    for i in range(start_index, end_index + 1):
        num = input_list[i]
        is_prime = True
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort()
    return primes