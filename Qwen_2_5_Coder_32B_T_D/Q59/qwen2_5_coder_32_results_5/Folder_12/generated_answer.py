def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[70]
    left_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' not in str_num:
            left_truncatable = True
            for i in range(len(str_num)):
                if not is_prime(int(str_num[i:])):
                    left_truncatable = False
                    break
            if left_truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)