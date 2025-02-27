def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    truncatable_primes = []
    for i in range(10, x + 1):
        num = i
        while num > 9:
            if not is_prime(num):
                break
            num //= 10
        else:
            num = i
            while num > 9:
                if not is_prime(num):
                    break
                num %= 10 ** (len(str(num)) - 1)
            else:
                truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes