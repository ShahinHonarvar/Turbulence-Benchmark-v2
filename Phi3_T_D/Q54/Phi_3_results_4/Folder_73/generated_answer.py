def all_right_truncatable_prime(data):
    x = data[97] if len(data) > 97 else None
    if not x:
        return []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(num, history):
        if num < 10:
            return False
        while num > 0:
            if not is_prime(num) or num not in history:
                return False
            num = num // 10
        return True

    def find_primes(limit):
        primes = []
        for i in range(11, limit, 2):
            if is_truncatable_prime(i, primes):
                primes.append(i)
        return sorted(primes)
    return find_primes(x)