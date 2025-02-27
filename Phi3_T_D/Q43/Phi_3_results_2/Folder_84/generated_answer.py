def find_primes_between_indices(numbers):
    start_index, end_index = (830, 849)
    primes = []
    for num in numbers[start_index:end_index + 1]:
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    return sorted(primes)