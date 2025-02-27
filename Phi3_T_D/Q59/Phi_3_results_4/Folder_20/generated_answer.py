def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, primes_set):
    if n in primes_set:
        n_str = str(n)
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    return False

def all_left_truncatable_prime(nums):
    x = nums[100]
    primes_set = set()
    left_truncatable_primes = []
    for number in range(x - 1, 0, -1):
        if is_prime(number) and is_left_truncatable_prime(number, primes_set):
            primes_set.add(number)
            left_truncatable_primes.append(number)
    return left_truncatable_primes