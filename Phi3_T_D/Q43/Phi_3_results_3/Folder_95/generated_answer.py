def find_primes_between_indices(numbers):
    primes = []
    for n in numbers[18:72]:
        if n > 1:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    break
            else:
                primes.append(n)
    return sorted(primes)