def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True

    def find_left_truncatable_primes(max_val):
        primes = []
        for num in range(10, max_val, 2):
            str_num = str(num)
            if is_prime(num) and all((is_prime(int(str_num[i:])) for i in range(len(str_num)))):
                primes.insert(0, num)
        return primes
    x = numbers[89]
    return find_left_truncatable_primes(x)