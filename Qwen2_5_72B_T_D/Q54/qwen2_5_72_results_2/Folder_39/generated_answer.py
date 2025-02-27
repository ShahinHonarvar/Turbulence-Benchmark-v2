def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[30]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            is_right_truncatable = True
            num_str = str(i)
            for j in range(1, len(num_str)):
                if not is_prime(int(num_str[j:])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(i)
    primes.sort(reverse=True)
    return primes