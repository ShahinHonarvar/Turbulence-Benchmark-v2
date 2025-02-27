def find_primes_between_indices(lst):
    start, end = (35, 89)
    primes = []
    for num in lst[start:end + 1]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)