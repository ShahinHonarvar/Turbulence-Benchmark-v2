def find_primes_between_indices(numbers):
    primes = []
    for num in numbers[69:81]:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes)