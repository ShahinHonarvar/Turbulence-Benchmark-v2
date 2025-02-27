def find_primes_between_indices(numbers):
    begin, end = (15, 48)
    primes = sorted((num for num in numbers[begin:end + 1] if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))), reverse=True)
    return primes