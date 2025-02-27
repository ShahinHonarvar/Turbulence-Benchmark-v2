def all_right_truncatable_prime(nums: tuple) -> list:
    x = nums[175]

    def is_truncatable_prime(num: int) -> bool:
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = []
    for num in range(2, x):
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result)