def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[784]
    truncatable_primes = []
    primes = set([2, 3, 5, 7])
    for num in range(x, 0, -1):
        num_str = str(num)
        if all((int(num_str[i:j + 1]) in primes for i in range(len(num_str)) for j in range(i, len(num_str)))) and is_prime(num):
            truncatable_primes.append(num)
            primes.add(num)
    return sorted(truncatable_primes)