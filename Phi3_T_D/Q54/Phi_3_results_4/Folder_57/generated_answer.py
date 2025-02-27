def all_right_truncatable_prime(nums):
    x = nums[54]
    prime_list = [i for i in range(2, x) if is_prime(i)]

    def is_right_truncatable(number, primes):
        str_num = str(number)
        for i in range(len(str_num)):
            if int(str_num[i:]) not in primes:
                return False
        return True
    right_truncatable_primes = [prime for prime in prime_list if is_right_truncatable(prime, prime_list)]
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True