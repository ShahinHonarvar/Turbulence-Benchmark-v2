def find_primes_between_indices(int_list):
    primes = []
    for numbers in int_list[55:88]:
        if numbers > 1:
            for i in range(2, int(numbers ** 0.5) + 1):
                if numbers % i == 0:
                    break
            else:
                primes.append(numbers)
    return sorted(primes)