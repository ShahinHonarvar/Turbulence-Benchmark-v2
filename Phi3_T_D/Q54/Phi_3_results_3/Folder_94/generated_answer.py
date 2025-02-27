def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    right_truncatable_primes = []
    for num in range(2, numbers[43]):
        original_num = num
        while num > 0:
            if not is_prime(num):
                break
            num = num // 10
        if num == 0:
            right_truncatable_primes.append(original_num)
    return sorted(right_truncatable_primes)