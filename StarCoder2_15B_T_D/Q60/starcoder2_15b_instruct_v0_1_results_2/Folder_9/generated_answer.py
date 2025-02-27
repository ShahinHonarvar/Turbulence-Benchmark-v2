def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num: int) -> bool:
    if num < 10:
        return is_prime(num)
    if num % 10 == 0:
        return False
    return is_left_right_truncatable_prime(int(num / 10)) and is_prime(num)

def all_left_right_truncatable_prime(nums: tuple) -> list:
    result = []
    for num in nums:
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)