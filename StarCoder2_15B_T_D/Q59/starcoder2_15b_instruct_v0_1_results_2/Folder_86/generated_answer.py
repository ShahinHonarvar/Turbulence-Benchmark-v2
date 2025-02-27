import math

def all_left_truncatable_prime(numbers):
    x = numbers[126]
    is_prime = [True] * x
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(x)) + 1):
        if is_prime[i]:
            for j in range(i * i, x, i):
                is_prime[j] = False
    left_truncatable_primes = []
    for i in range(x):
        if is_prime[i]:
            number_str = str(i)
            if '0' not in number_str:
                is_left_truncatable = True
                for j in range(1, len(number_str)):
                    if not is_prime[int(number_str[j:])]:
                        is_left_truncatable = False
                        break
                if is_left_truncatable:
                    left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)