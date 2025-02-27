def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes_set):
        if n not in primes_set:
            return False
        if n < 10:
            return True
        return is_right_truncatable_prime(n // 10, primes_set)
    x = numbers[645]
    primes_set = set()
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            primes_set.add(num)
            for rt_length in range(len(str(num)), 1, -1):
                rt_num = int(str(num)[:-rt_length])
                if is_right_truncatable_prime(rt_num, primes_set):
                    right_truncatable_primes.append(rt_num)
    return sorted(set(right_truncatable_primes))