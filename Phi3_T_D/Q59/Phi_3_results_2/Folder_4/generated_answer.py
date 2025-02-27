def all_left_truncatable_prime(numbers):
    x = numbers[96]
    primes = [2, 3, 5, 7]
    added_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in primes:
            if i * i > n:
                break
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, primes):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    for potential in range(7, x):
        if potential not in added_primes and str(potential).startswith(('2', '3', '5', '7')):
            if is_left_truncatable(potential, primes):
                added_primes.append(potential)
                primes.append(potential)
    added_primes.sort(reverse=True)
    return added_primes