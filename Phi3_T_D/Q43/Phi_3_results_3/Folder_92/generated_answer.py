def find_primes_between_indices(numbers):
    prime_numbers = []
    start, end = (7, 8)
    for num in numbers[start:end + 1]:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)
    return sorted(prime_numbers)