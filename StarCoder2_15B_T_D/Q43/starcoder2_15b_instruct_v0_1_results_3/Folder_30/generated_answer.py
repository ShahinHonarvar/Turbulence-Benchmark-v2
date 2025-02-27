def find_primes_between_indices(numbers):
    primes = []
    for i, num in enumerate(numbers):
        if i < 61 or i > 80:
            continue
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)