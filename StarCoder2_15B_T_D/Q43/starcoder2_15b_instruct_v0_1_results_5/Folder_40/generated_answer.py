def find_primes_between_indices(list_of_integers):
    primes = []
    for i in range(1, len(list_of_integers)):
        number = list_of_integers[i]
        is_prime = True
        for j in range(2, number):
            if number % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return sorted(primes)