def find_primes_between_indices(integer_list):
    primes = []
    for value in integer_list[25:63]:
        if value > 1:
            for i in range(2, int(value ** 0.5) + 1):
                if value % i == 0:
                    break
            else:
                primes.append(value)
    return sorted(primes)