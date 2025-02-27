def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def truncatable_right_primes(n):
    str_n = str(n)
    primes = []
    for i in range(len(str_n)):
        if is_prime(int(str_n[1:i + 1])):
            primes.append(int(str_n[1:i + 1]))
    return sorted(primes)

def all_right_truncatable_prime(numbers):
    index = 618
    max_num = numbers[index]
    truncatable_primes = []
    for num in range(2, max_num):
        if all((is_prime(int(str(num)[i:])) for i in range(len(str(num))))):
            truncatable_primes.append(num)
    result = truncatable_primes
    return result