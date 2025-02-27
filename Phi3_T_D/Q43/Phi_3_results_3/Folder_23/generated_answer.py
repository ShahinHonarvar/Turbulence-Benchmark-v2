def find_primes_between_indices(numbers):
    return sorted([x for x in numbers[20:49] if x > 1 and all((x % i != 0 for i in range(2, int(x ** 0.5) + 1)))], reverse=True)