def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def ends_with_prime(n, digit):
    return is_prime(int(str(n) + str(digit)))

def get_truncatable_primes(x):
    truncatable_primes = []
    for i in range(10, x + 1, 2):
        str_i = str(i)
        prime = True
        for j in range(len(str_i)):
            if not ends_with_prime(i // 10 ** j, int(str_i[0])) or not ends_with_prime(i, int(str_i[j])):
                prime = False
                break
        if prime:
            truncatable_primes.append(i)
    return truncatable_primes

def all_left_right_truncatable_prime(numbers):
    x = numbers[26]
    return get_truncatable_primes(x)