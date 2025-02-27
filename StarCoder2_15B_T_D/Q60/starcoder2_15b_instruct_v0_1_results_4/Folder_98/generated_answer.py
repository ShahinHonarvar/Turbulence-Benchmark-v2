def is_truncatable_prime(num: int) -> bool:
    if num < 10:
        return num in (2, 3, 5, 7)
    return is_truncatable_prime(num % 10) and is_truncatable_prime(num // 10) and is_prime(num)

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums: tuple) -> list:
    x = nums[8]
    result = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)