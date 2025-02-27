def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def truncatable_primes(primes, x):
        result = []
        for prime in primes:
            if prime >= x:
                continue
            prime_str = str(prime)
            is_truncatable = True
            for i in range(1, len(prime_str)):
                if not is_prime(int(prime_str[:-i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(prime)
            if len(result) == 10:
                break
        return result[::-1]
    x = numbers[54]
    truncatable_primes_list = [2, 3, 5, 7]
    for num in range(11, x):
        if is_prime(num) and num % 10 in [2, 3, 5, 7]:
            truncatable_primes_list.append(num)
    return truncatable_primes(truncatable_primes_list, x)