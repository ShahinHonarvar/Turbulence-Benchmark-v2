def find_primes_between_indices(int_list):
    primes = []
    for number in int_list[23:49]:
        if all((number % i != 0 for i in range(2, int(number ** 0.5) + 1))) and number > 1:
            primes.append(number)
    return sorted(primes)