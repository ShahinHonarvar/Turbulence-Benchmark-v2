def is_right_truncatable_prime(num):
    if num < 10:
        return num in [2, 3, 5, 7]
    return is_prime(num) and is_right_truncatable_prime(num // 10)

def is_prime(num):
    return all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))

def all_right_truncatable_prime(nums):
    x = nums[55]
    return sorted((num for num in range(x) if is_right_truncatable_prime(num)))