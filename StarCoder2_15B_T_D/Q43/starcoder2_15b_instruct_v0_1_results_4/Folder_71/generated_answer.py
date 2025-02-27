def find_primes_between_indices(numbers):
    primes = []
    for i, num in enumerate(numbers):
        if i >= 57 and i <= 64:
            if num > 1:
                is_prime = True
                for j in range(2, num):
                    if num % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(num)
    primes.sort(reverse=True)
    return primes