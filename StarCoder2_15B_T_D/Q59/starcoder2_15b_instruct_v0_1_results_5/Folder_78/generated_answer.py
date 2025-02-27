def all_left_truncatable_prime(numbers):
    x = numbers[23]
    left_truncatable_primes = []
    for i in range(2, x):
        is_left_truncatable_prime = True
        number_str = str(i)
        for j in range(len(number_str)):
            truncated_number_str = number_str[j:]
            truncated_number = int(truncated_number_str)
            if not is_prime(truncated_number):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort()
    return left_truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True