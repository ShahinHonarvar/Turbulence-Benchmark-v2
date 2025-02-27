def find_primes_between_indices(int_list):
    primes = []
    for number in int_list[46:62]:
        if number > 1:
            is_prime = True
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(number)
    return sorted(primes)