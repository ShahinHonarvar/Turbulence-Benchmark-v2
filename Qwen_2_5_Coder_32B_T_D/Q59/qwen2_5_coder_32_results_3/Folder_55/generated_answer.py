def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[73]
    lt_primes = []
    for num in range(2, x):
        num_str = str(num)
        if '0' not in num_str:
            all_prime = True
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])):
                    all_prime = False
                    break
            if all_prime and is_prime(num):
                lt_primes.append(num)
    return sorted(lt_primes, reverse=True)