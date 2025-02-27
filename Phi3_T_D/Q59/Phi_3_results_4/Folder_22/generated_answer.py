def all_left_truncatable_prime(nums):
    max_num = nums[85]
    primes = [2, 3, 5, 7]
    for num in range(11, max_num):
        if all((num % prime != 0 for prime in primes)):
            primes.append(num)

    def is_left_truncatable(prime):
        str_prime = str(prime)
        while str_prime:
            if int(str_prime) not in primes:
                return False
            str_prime = str_prime[1:]
        return True
    left_truncatable_primes = [prime for prime in primes if is_left_truncatable(prime) and len(str(prime)) > 1]
    return left_truncatable_primes