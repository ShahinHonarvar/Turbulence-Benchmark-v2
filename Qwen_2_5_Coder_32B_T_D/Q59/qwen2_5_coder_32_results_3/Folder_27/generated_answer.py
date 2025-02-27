def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[79]
    left_truncatable_primes = []
    for num in range(10, x):
        num_str = str(num)
        if '0' not in num_str:
            truncatable = True
            for i in range(len(num_str)):
                if not is_prime(int(num_str[i:])):
                    truncatable = False
                    break
            if truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)