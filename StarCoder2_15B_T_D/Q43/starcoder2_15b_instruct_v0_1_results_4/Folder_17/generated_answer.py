def find_primes_between_indices(numbers):
    output = []
    for i, num in enumerate(numbers):
        if i >= 15 and i <= 48:
            is_prime = True
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    is_prime = False
                    break
            if is_prime:
                output.append(num)
    output.sort(reverse=True)
    return output