def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(args):
    x = args[4]
    right_truncatable_primes = []

    def helper(number, digits):
        if number == 0 or number < 2:
            return False
        if is_prime(number) and number < x:
            if all((is_prime(int(str(number)[:i])) for i in range(1, len(str(number)) + 1))):
                right_truncatable_primes.append(number)
        return True
    for num in range(2, min(x, 10 ** 6)):
        helper(num, len(str(num)))
    return sorted(list(set(right_truncatable_primes)))