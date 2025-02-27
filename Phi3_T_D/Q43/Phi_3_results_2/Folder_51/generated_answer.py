def find_primes_between_indices(numbers):
    start, end = (14, 68)
    primes = []
    for number in numbers[start:end + 1]:
        if number > 1:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    break
            else:
                primes.append(number)
    return sorted(primes, reverse=True)