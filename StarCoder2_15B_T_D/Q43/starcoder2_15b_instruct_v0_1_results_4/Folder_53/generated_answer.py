def find_primes_between_indices(lst):
    prime_numbers = []
    for i, num in enumerate(lst):
        if is_prime(num) and 43 <= i <= 59:
            prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)

def is_prime(num):
    if num > 1:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True
    return False