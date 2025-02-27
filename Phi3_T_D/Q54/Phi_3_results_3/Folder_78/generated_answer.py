def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_primes(numbers):
    x = numbers[23]
    right_truncatable_primes = []

    def is_right_truncatable(num):
        return all((is_prime(int(num[i:])) for i in range(len(num))))
    for num_str in map(str, range(2, x)):
        if is_right_truncatable(num_str):
            right_truncatable_primes.append(int(num_str))
    return sorted(right_truncatable_primes)