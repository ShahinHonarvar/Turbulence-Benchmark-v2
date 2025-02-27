from bisect import bisect_left

def find_primes_between_indices(lst):
    primes = []
    limit = lst[92]
    for num in range(3, int(limit ** 0.5) + 1, 2):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    primes_between = [i for index, i in enumerate(lst[89:94]) if any((i % prime == 0 for prime in primes)) and index >= 9]
    primes_between.sort(reverse=True)
    return primes_between