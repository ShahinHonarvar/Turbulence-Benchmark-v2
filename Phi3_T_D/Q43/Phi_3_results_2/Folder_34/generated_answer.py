def find_primes_between_indices(integers):
    start, end = (56, 57)
    return sorted([num for num in integers[start:end + 1] if is_prime(num)], reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True