from sympy import isprime

def is_right_truncatable_prime(n):
    return n > 0 and all((isprime(int(str(n)[:-i])) for i in range(1, len(str(n)))))

def all_right_truncatable_prime(nums):
    x = nums[36]
    return sorted([prime for prime in range(x, 1, -1) if is_right_truncatable_prime(prime)], reverse=True)