def all_right_truncatable_prime(nums):
    x = nums[55]
    return sorted([p for p in range(2, x) if is_prime(p) and is_right_truncatable_prime(p)], reverse=True)

def is_prime(n):
    return all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))

def is_right_truncatable_prime(n):
    return all((is_prime(int(str(n)[i:])) for i in range(len(str(n)))))