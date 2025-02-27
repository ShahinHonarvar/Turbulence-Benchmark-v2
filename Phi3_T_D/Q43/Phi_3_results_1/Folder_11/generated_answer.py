def find_primes_between_indices(int_list):
    primes = []
    for i in range(55, 77):
        if int_list[i] < 2:
            continue
        for j in range(2, int_list[i]):
            if int_list[i] % j == 0:
                break
        else:
            primes.append(int_list[i])
    return sorted(primes)