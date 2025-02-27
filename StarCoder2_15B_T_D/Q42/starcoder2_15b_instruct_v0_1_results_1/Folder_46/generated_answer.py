def prime_factors(numbers):
    is_prime = [True] * (max(numbers) + 1)
    for i in range(2, int(max(numbers) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max(numbers) + 1, i):
                is_prime[j] = False
    prime_factors = {n: [] for n in numbers}
    for n in numbers:
        for i in range(2, n + 1):
            if is_prime[i] and n % i == 0:
                prime_factors[n].append(i)
    return prime_factors[numbers[453]]