def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, primes_set):
        if n in primes_set:
            str_n = str(n)
            for i in range(1, len(str_n)):
                if int(str_n[i:]) not in primes_set:
                    return False
            return True
        return False
    upper_limit = nums[55]
    all_primes = {2, 3, 5, 7}
    for num in range(10, upper_limit):
        if is_prime(num):
            all_primes.add(num)
    left_truncatable_primes = [num for num in all_primes if is_left_truncatable(num, all_primes)]
    return sorted(left_truncatable_primes, reverse=True)