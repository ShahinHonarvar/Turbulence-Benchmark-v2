def find_primes_between_indices(numbers):
    sliced_list = numbers[75:86]
    primes = [num for num in sliced_list if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))]
    primes.sort()
    return primes