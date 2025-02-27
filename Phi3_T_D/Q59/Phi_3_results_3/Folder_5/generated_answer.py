def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[55]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            string_number = str(i)
            j = 1
            while j < len(string_number):
                if not is_prime(int(string_number[j:])):
                    break
                j += 1
            else:
                primes.append(i)
    return primes