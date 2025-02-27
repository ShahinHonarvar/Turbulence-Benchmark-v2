def all_right_truncatable_prime(numbers):
    x = numbers[10]
    truncatable_primes = []
    for i in range(2, x):
        is_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            truncated_number = int(str(i)[j + 1:])
            if not is_prime(truncated_number):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True