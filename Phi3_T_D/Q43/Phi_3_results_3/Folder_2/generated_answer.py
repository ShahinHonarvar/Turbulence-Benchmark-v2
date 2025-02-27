def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    prime_list = [num for i, num in enumerate(numbers) if 167 <= i <= 785 and is_prime(num)]
    prime_list.sort(reverse=True)
    return prime_list