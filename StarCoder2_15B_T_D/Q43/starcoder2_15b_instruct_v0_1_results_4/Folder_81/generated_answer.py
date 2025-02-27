def find_primes_between_indices(input_list):
    numbers = input_list[59:98]
    primes = [n for n in numbers if is_prime(n)]
    primes.sort(reverse=True)
    return primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True