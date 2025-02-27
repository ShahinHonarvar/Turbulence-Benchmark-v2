def prime_factors(numbers):
    if len(numbers) > 851 and numbers[851] > 0:
        is_prime = [True] * (numbers[851] + 1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, int(numbers[851] ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, numbers[851] + 1, i):
                    is_prime[j] = False
        return [i for i in range(numbers[851] + 1) if is_prime[i]]
    else:
        return []