def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num, primes):
        once_removed = str(num)[1:]
        return once_removed not in primes and is_prime(int(once_removed))
    x = numbers[50]
    primes = [2, 3, 5, 7]
    result = []
    for num in range(x - 1, 0, -1):
        if is_prime(num) and is_left_truncatable_prime(num, primes):
            primes.insert(0, num)
            result.append(num)
    return result