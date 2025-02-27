def all_left_truncatable_prime(numbers):
    x = numbers[429]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if all((num % prime != 0 for prime in primes)):
            primes.append(num)
    left_truncatable = []
    for prime in primes:
        str_prime = str(prime)
        temp_prime = prime
        while len(str_prime) > 1:
            if temp_prime % 10 == 0 or not is_prime(temp_prime):
                break
            temp_prime = temp_prime // 10
            str_prime = str_prime[1:]
        if len(str_prime) == 1 and is_prime(prime):
            left_truncatable.append(prime)
    return sorted(left_truncatable, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True