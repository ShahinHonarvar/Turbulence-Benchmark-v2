def all_left_truncatable_prime(max_num):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, primes):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
            if str_n[i] == '0':
                return False
            if not int(str_n[i]) in primes:
                return False
        return True
    primes = [2]
    results = []
    for number in range(3, max_num, 2):
        if is_prime(number):
            primes.append(number)
            if is_left_truncatable(number, primes):
                results.append(number)
    return sorted(results, reverse=True)