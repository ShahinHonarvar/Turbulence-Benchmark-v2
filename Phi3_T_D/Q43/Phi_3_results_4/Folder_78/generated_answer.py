def find_primes_between_indices(lst):
    primes = []
    for number in lst[27:83 + 1]:
        prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                prime = False
                break
        if prime and number > 1:
            primes.append(number)
    return sorted(primes)